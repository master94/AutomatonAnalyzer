from collections import namedtuple

from automaton import Automaton


AutomatonTest = namedtuple('AutomatonTest', ['automaton', 'valid_strings', 'invalid_strings'])

at1 = AutomatonTest(
        automaton = Automaton('aaa - automaton', 4, { 0: {'a': 1}, 1: {'a': 2}, 2: {'a': 3, 'b': 2}, 3: {'c': 3} }, 0, 3),
        valid_strings = ['aaa', 'aabac', 'aabbac', 'aabba', 'aabacc', 'aabbbbbbbbbbbbbbbbbacccccccc'],
        invalid_strings = ['aa', 'aaaa', 'a', '', 'cc', 'bb', 'aabb', 'aacc']
      )


def get_test_data():
    return [at1]
