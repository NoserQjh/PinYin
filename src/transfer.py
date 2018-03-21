# coding=utf-8
# encoding=utf8
import math
import re

import state


def update_states(last_states, next_character, datanum, unit_lambda):
    next_states = set()
    for word in next_character.words:
        this_state = state.State(word)
        this_state.p = -10000
        next_states.add(this_state)

    for next_state in next_states:
        for last_state in last_states:
            next_word = next_state.last_word
            last_word = last_state.last_word

            self_p = (next_word.appearence + 0.1) / datanum
            unit_p = float(next_word.ahead.setdefault(last_word.spell, 0)) / float(
                last_word.appearence + 1) * unit_lambda
            plus_p = math.log(self_p + unit_p)

            next_p = last_state.p + plus_p

            if next_p > next_state.p:
                next_state.p = next_p
                next_state.sent = last_state.sent + next_word.spell

    return next_states


def transfer(input_path, output_path, spell2character, datanum, unit_lambda):
    print('\nTransfering...')
    with open(unicode(input_path, "utf-8"), 'r') as in_fr:
        with open(unicode(output_path, "utf-8"), 'w ') as out_fr:
            for line in in_fr:
                # clean text
                line_result = u''
                line = line.decode('GBK')
                line = line.strip('\n')
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
                        line_result = states[0].sent
                        print>> out_fr, line_result.encode('GBK')
                    else:
                        print('Error! spell = ' + line[0])
