# coding=utf-8
# encoding=utf8

import config
from train import *
from transfer import *

conf = config.Config()

if __name__ == '__main__':
    # train
    train(conf=conf)

    # load
    words, spell2word, characters, spell2character = load_from_saved(path=conf.save_path)

    transfer(input_path=conf.input_path, output_path=conf.output_path, spell2character=spell2character,
             datanum=conf.data_num)

    print('Success!')

    # os.system("pause")
