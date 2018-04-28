# coding=utf-8
# encoding=utf8

import sys

import config
from load import *
from transfer import *

conf = config.Config()


def test(input_path, output_path, character_list_path, spell2character, datanum):
    word2character = load_word2character(character_list_path)
    dataset = load_dataset(input_path)
    with open(input_path + '/testfile/test.txt', 'w') as fr:
        for x in dataset:
            print >> fr, x.encode('GBK')
    with open(input_path + '/testfile/test_pinyin.txt', 'w') as frpinyin:
        with open(input_path + '/testfile/test.txt', 'w') as fr:
            for i in range(0, 1000):
                x = dataset[i]
                pinyin = u''
                sent = u''
                for j in x:
                    character = word2character.setdefault(j, None)
                    if character:
                        pinyin = pinyin + character + ' '
                        sent = sent + j
                print>> frpinyin, pinyin.encode('GBK')
                print>> fr, sent.encode('GBK')
    for i in range(30, 31):
        unit_lambda = i
        start_time = time.time()
        transfer(input_path=input_path + '/testfile/test_pinyin.txt', output_path=output_path,
                 spell2character=spell2character, datanum=datanum, unit_lambda=unit_lambda)
        num_same = 0
        num_all = 0
        with open(input_path + '/testfile/test.txt', 'r') as fri:
            with open(output_path, 'r') as fro:
                while 1:
                    line1 = fri.readline()
                    line2 = fro.readline()
                    if not line1:
                        break
                    if not line2:
                        break
                    line1 = line1.decode('GBK')
                    line2 = line2.decode('GBK')
                    line1.strip('\n')
                    line2.strip('\n')
                    if len(line1) != len(line2):
                        # print('Error')
                        line1 = fri.readline()
                    else:
                        num_all = num_all + len(line1)
                        for i in range(len(line1)):
                            if (line1[i] == line2[i]):
                                num_same = num_same + 1
        print('Unit_lambda:%02d' % unit_lambda)
        print('\tAccuracy rate: %02.3f' % (float(num_same) / float(num_all)))
        print("\tTook: %4.4fs" % (time.time() - start_time))
    return num_same / num_all


if __name__ == '__main__':
    # train
    # train(conf=conf)

    # load
    spell2character = []
    words, spell2word, characters, spell2character = load_from_saved(path=conf.save_path)

    if len(sys.argv) == 1:
        input_path = conf.input_path
        output_path = conf.output_path
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]

    transfer(input_path=input_path, output_path=output_path, spell2character=spell2character,
             datanum=conf.data_num, unit_lambda=conf.unit_lambda)

    # test
    # test(input_path=conf.test_path, output_path=conf.output_path, character_list_path=conf.character_list_path,
    #    spell2character=spell2character, datanum=conf.data_num)
    # print('Success!')
    os.system("pause")
