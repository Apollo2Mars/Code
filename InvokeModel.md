- Plan A
  - python
        builder = tf.saved_model.builder.SavedModelBuilder("/tmp/model" )
        builder.add_meta_graph_and_variables(
          sess,
          [tf.saved_model.tag_constants.SERVING]
        )
        builder.save()
  - java
        SavedModelBundle b = SavedModelBundle.load("/tmp/model", "serve");
  - example
        # good idea
        # https://stackoverflow.com/documentation/tensorflow/10718/save-tensorflow-model-in-python-# and-load-with-java#t=201709030336395954421
        
        import tensorflow as tf
        tf.reset_default_graph()
        # DO MODEL STUFF
        # Pretrained weighting of 2.0
        W = tf.get_variable('w', initializer=tf.constant(2.0), dtype=tf.float32)
        # Model input x
        x = tf.placeholder(tf.float32, name='x')
        # Model output y = W*x
        y = tf.multiply(W, x, name='y')
        # DO SESSION STUFF
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        # SAVE THE MODEL
        builder = tf.saved_model.builder.SavedModelBuilder("/tmp/model" )
        builder.add_meta_graph_and_variables(
          sess,
          [tf.saved_model.tag_constants.SERVING]
        )
        builder.save()
        
        import org.tensorflow.SavedModelBundle;
        import org.tensorflow.Session;
        import org.tensorflow.Tensor;
        import org.tensorflow.TensorFlow;
        import java.io.IOException;
        import java.nio.FloatBuffer;
        /**
        - Created by apollo on 17-9-3.
        - https://stackoverflow.com/documentation/tensorflow/10718/save-tensorflow-model-in-python-and-load-with-java#t=201709030336395954421
          */
          public class LoadModel {
          public static void main(String[] args) throws IOException {
              // good idea to print the version number, 1.2.0 as of this writing
              System.out.println(TensorFlow.version());
              final int NUM_PREDICTIONS = 1;   
              /* load the model Bundle */
              SavedModelBundle b = SavedModelBundle.load("/tmp/model", "serve");
              
              // create the session from the Bundle
              Session sess = b.session();
              // create an input Tensor, value = 2.0f
              Tensor x = Tensor.create(
                      new long[]{NUM_PREDICTIONS},
                      FloatBuffer.wrap(new float[]{2.0f})
              );
              
              // run the model and get the result, 4.0f.
              float[] y = sess.runner()
                      .feed("x", x)
                      .fetch("y")
                      .run()
                      .get(0)
                      .copyTo(new float[NUM_PREDICTIONS]);
              
              // print out the result.
              System.out.println(y[0]);
          }
          }
- Plan B
      On the Python side, Tensorflow suggests to use a Saver object to save a model to disk. It creates a .meta file that has the definition and has .data files for the weights. In Python, I use new_saver=tf.train.import_meta_graph(var_filename)
      
        new_saver.restore(sess, model_filename) to read the model from the disk.
      

- Plan C
      # only in python, only save
      tf.train.write_graph(sess.graph_def, "./data", "aaa.pb");
      this aaa.pb contains graph and variables , not like Plan A(that pb only contain graph)
