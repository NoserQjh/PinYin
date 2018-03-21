# coding=utf-8
# encoding=utf8

import config
from load import *
from transfer import *

conf = config.Config()


def transfer_sent(sent, spell2character, datanum, unit_lambda):
    line = sent.strip('\n')
    line = re.split(u'[\s]', line)
    if len(line) > 0:
        # create state
        this_character = spell2character.setdefault(line[0], None)
        if this_character:
            states = set()
            for word in this_character.words:
                this_state = state.State(word)
                this_state.p = math.log((word.appearence + 0.1) / datanum)
                this_state.sent = this_state.sent + word.spell
                states.add(this_state)
            for i in range(len(line) - 1):
                this_character = spell2character.setdefault(line[i + 1], None)
                if this_character:
                    states = update_states(last_states=states, next_character=this_character,
                                           datanum=datanum, unit_lambda=unit_lambda)
            states = list(states)
            states.sort(key=lambda x: x.p, reverse=True)
            for x in states:
                print(u'p:%4.4f' % x.p + x.sent)


if __name__ == '__main__':
    # train
    # train(conf=conf)

    # load
    words, spell2word, characters, spell2character = load_from_saved(path=conf.save_path)

    '''transfer(input_path=conf.input_path, output_path=conf.output_path, spell2character=spell2character,
             datanum=conf.data_num)
    '''

    while True:
        sent = raw_input("Input:")
        transfer_sent(sent=sent, spell2character=spell2character, datanum=conf.data_num, unit_lambda=conf.unit_lambda)

    print('Success!')

    # os.system("pause")
