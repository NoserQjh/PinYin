# coding=utf-8
# encoding=utf8
import glob
import os
import pickle
import re
import time

import character


def load_from_saved(path):
    print('\nLoading from saved...')
    start_time = time.time()
    words, spell2word, characters, spell2character = pickle.load(open(path, 'rb'))
    print("\tLoading from saved took: %4.4fs" % (time.time() - start_time))
    return words, spell2word, characters, spell2character


def load_basements(word_list_path, character_list_path):
    # load basements
    words, spell2word = load_word_list(path=word_list_path)
    characters, spell2character = load_character_list(path=character_list_path,
                                                      spell2word=spell2word)

    return words, spell2word, characters, spell2character


def load_word_list(path):
    print('\nLoading word list...')
    words = set()
    spell2word = dict()
    with open(unicode(path, "utf-8"), 'r') as fr:
        for line in fr:
            line = line.decode('GBK')
            line = line.strip('\n')
            for word in line:
                this_word = character.Word(word)
                words.add(this_word)
                spell2word[word] = this_word
    return words, spell2word


def load_character_list(path, spell2word):
    print('\nLoading character list...')
    characters = set()
    spell2character = dict()

    with open(unicode(path, "utf-8"), 'r') as fr:
        for line in fr:
            line = line.decode('GBK')
            line = line.strip('\n')
            line = line.split(' ')
            this_character = character.Character(line[0])
            for i in range(len(line) - 1):
                this_character.words.add(spell2word.setdefault(line[i + 1], None))
            characters.add(this_character)
            spell2character[this_character.spell] = this_character
    return characters, spell2character


def load_dataset(path):
    print('\nLoading dataset...')
    files = glob.glob(os.path.join(path, "*"))
    files = [f for f in files if re.search("11.txt$", os.path.basename(f))]
    dataset = list()
    start_time = time.time()
    for file in files:
        with open(unicode(file, "utf-8"), 'r') as fr:
            for line in fr:
                line = line.decode('GBK')
                line = re.split(
                    u'[\\\\@a-zA-Z0-9\-/‚()【】\[\]（）,.，。！!？?~～：:；;…=\s\n\r\t{}"、<>《》℃%“”·#_’‘\'■％—|－+□○●▲＋→]', line)
                line = list(set(line))
                line.remove(u'')
                dataset.extend(line)
    print("\tLoading dataset took: %4.4fs" % (time.time() - start_time))
    return dataset
