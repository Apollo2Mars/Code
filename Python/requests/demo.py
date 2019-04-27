#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-26 15:20
# @Author  : apollo2mars
# @File    : main.py
# @Contact : apollo2mars@gmail.com
# @Desc    : requests demo
import requests
import pandas as pd


def read_data(input_file):
	df = pd.read_excel(input_file, encoding='utf-8', usecols=0)
	return list(df.get_values())


def request(input_list):
	for item in input_list:
		result = requests.get('http://aaaa' + str(item))
		print(item)
		print(result.text)


item_list = read_data('data/data_1.xlsx')
request(item_list)