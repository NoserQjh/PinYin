#!/usr/bin/python
# -*- coding: utf-8 -*-


class Character(object):
    # 字类
    def __init__(self, spell):
        self.spell = spell
        self.words = set()


class Word(object):
    # 汉字
    def __init__(self, spell):
        self.spell = spell
        self.appearence = 0
        self.follow = dict()
        self.ahead = dict()
