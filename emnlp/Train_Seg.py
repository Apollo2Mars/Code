# coding: UTF-8

import os
import logging
import sys
from neuralnets.BiLSTM import BiLSTM
from util.preprocessing import perpareDataset, loadDatasetPickle

# :: Change into the working dir of the script ::
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# :: Logging level ::
loggingLevel = logging.INFO
logger = logging.getLogger()
logger.setLevel(loggingLevel)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(loggingLevel)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

#####################################################
#
# Set special GPU
#
#####################################################

os.environ["CUDA_VISIBLE_DEVICES"] = "8,9"


######################################################
#
# Input parameters settings
#
######################################################
# datasetName = 'hk_seg'
datasetName = 'zh_seg'
dataColumns = {0:'tokens', 1:'SEG'}     # Tab separated columns, column 1 contains the token, 3 the universal POS tag
labelKey = 'SEG'
embeddingsPath = 'emptyEmb.txt'  # now is empty embeddings, random vector will generate later

######################################################
#
#  Prepares the dataset to be used with the LSTM-network. Creates and stores cPickle files in the pkl/ folder
#
######################################################

datasetFiles = [
        (datasetName, dataColumns),
    ]
frequencyThresholdUnknownTokens = 0  # If a token that is not in the pre-trained embeddings file appears at least 50 times in the train.txt, then a new embedding is generated for this word
pickleFile = perpareDataset(embeddingsPath, datasetFiles, frequencyThresholdUnknownTokens)
embeddings, word2Idx, datasets = loadDatasetPickle(pickleFile)  # Load the embeddings and the dataset
data = datasets[datasetName]    # datasets[SEG] or datasets[[POS]
#
# datasets
# 	- hk_seg
# 		- mappings
# 			-	SEG	{'I': 4, 'S': 3, 'B': 1, 'E': 2, 'O': 0}       # All seg set
# 			-	tokens	{u'\u8000': 1607, ......, u'\u8bf8': 5161}	# All tokens
# 		- testMatrix
# 		- trainMatrix
# 		- devMatrix
# 			-	00001
# 				-	SEG	<type 'list'>: [1, 2, 3, 1, 2, 3, 3, 3]
# 				-	raw_tokens	<type 'list'>: [u'\u5ee0', u'\u623f', u'\u55ba', u'\u4e0a', u'\u6d77', u'\u7b49', u'\u5730', u'\u3002']
# 				-	tokens	<type 'list'>: [922, 808, 66, 52, 234, 146, 35, 6]
# 			-	00002
# 			......
#

print("Dataset:", datasetName)
print(data['mappings'].keys())
print("Label key: ", labelKey)  # 'seg or pos'
print("Train Sentences:", len(data['trainMatrix']))
print("Dev Sentences:", len(data['devMatrix']))
print("Test Sentences:", len(data['testMatrix']))


# Parameters of the network
params = {'dropout': [0.5, 0.5], 'classifier': 'CRF', 'LSTM-Size': [1024], 'optimizer': 'nadam', 'charEmbeddings': None, 'miniBatchSize': 32}

model = BiLSTM(params)
model.setMappings(embeddings, data['mappings'])
model.setTrainDataset(data, labelKey)   # datasets[SEG] and SEG
model.verboseBuild = True
model.modelSavePath = "models/%s/%s/[DevScore]_[TestScore]_[Epoch].h5" % (datasetName, labelKey)    # Enable this line to save the model to the disk
model.evaluate(100)


