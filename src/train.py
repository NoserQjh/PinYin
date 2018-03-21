# coding=utf-8
# encoding=utf8

from load import *


def train_dataset(dataset, spell2word):
    print('\nTraining...')
    start_time = time.time()
    for num in range(len(dataset)):
        x = dataset[num]
        length = len(x)
        for i in range(length):
            this_word = spell2word.setdefault(x[i], None)
            if this_word:
                this_word.appearence = this_word.appearence + 1
                if i != 0:
                    ahead = spell2word.setdefault(x[i - 1], None)
                    if ahead:
                        this_word.ahead[ahead.spell] = this_word.ahead.setdefault(ahead.spell, 0) + 1
                if i != length - 1:
                    follow = spell2word.setdefault(x[i + 1], None)
                    if follow:
                        this_word.follow[follow.spell] = this_word.follow.setdefault(follow.spell, 0) + 1
    print("\tTraining took: %4.4fs" % (time.time() - start_time))


def train(conf):
    words, spell2word, characters, spell2character = load_basements(word_list_path=conf.word_list_path,
                                                                    character_list_path=conf.character_list_path)

    # load dataset
    dataset = load_dataset(path=conf.dataset_path)

    # train
    train_dataset(dataset=dataset, spell2word=spell2word)

    # save
    print('\nSaving...')
    start_time = time.time()
    pickle.dump([words, spell2word, characters, spell2character], open(conf.save_path, 'wb'))
    print("\tSaving took: %4.4fs" % (time.time() - start_time))
