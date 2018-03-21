#!/usr/bin/python
# -*- coding: utf-8 -*-


class State(object):
    # 字类
    def __init__(self, last_word):
        self.last_word = last_word
        self.p = 0
        self.sent = u''
