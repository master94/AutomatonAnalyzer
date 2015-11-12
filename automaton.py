class Automaton:
    def __init__(self, name, states, transitions, start_state, finish_state):
        self.__name = name
        self.__states = states
        self.__transitions = transitions
        self.__start_state = start_state
        self.__finish_state = finish_state

    def name(self):
        return self.__name

    def states_count(self):
        return self.__states

    def start(self):
        return self.__start_state

    def finish(self):
        return self.__finish_state

    def transitions(self):
        return self.__transitions

    def accepts(self, word):
        st = self.__start_state

        for x in word:
            new_state = self.__transitions[st].get(x, None)
            if new_state is None:
                return False
            st = new_state

        return st == self.__finish_state
