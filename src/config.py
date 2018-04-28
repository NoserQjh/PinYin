#!/usr/bin/python
# -*- coding: utf-8 -*-
class Config(object):
    # 基本设置
    def __init__(self):
        self.character_list_path = '../lib/拼音汉字表.txt'
        self.word_list_path = '../lib/一二级汉字表.txt'
        self.dataset_path = '../dataset'
        self.save_path = '../save.txt'
        self.input_path = '../data/input.txt'
        self.output_path = '../data/output.txt'
        self.test_path = '../test'

        self.k = 2
        self.data_num = 60512929
        self.unit_lambda = 300
