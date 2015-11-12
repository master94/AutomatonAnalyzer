from collections import namedtuple

from automaton import Automaton


AutomatonTest = namedtuple('AutomatonTest', ['automaton', 'valid_strings', 'invalid_strings'])

at1 = AutomatonTest(
        automaton = Automaton('aaa - automaton', 4, { 0: {'a': 1}, 1: {'a': 2}, 2: {'a': 3, 'b': 2}, 3: {'c': 3} }, 0, 3),
        valid_strings = ['aaa', 'aabac', 'aabbac', 'aabba', 'aabacc', 'aabbbbbbbbbbbbbbbbbacccccccc'],
        invalid_strings = ['aa', 'aaaa', 'a', '', 'cc', 'bb', 'aabb', 'aacc']
      )


at2 = AutomatonTest(
	automaton = Automaton('ab*cd*ef* - automaton', 4, { 0: {'a': 1}, 1: {'b': 1, 'c': 2}, 2: {'d': 2, 'e': 3}, 3: {'f': 3} }, 0, 3),
        valid_strings = ['ace', 'abce', 'abbbbbbbce', 'acddddddddde', 'aceffffffffff', 'abbbbbcddddddddefffffffff', 'abcdef'],
        invalid_strings = ['aa', 'aaaa', 'a', '', 'cc', 'bb', 'aabb', 'aacc', 'abcdf']
      )


at3 = AutomatonTest(
	automaton = Automaton('a*bc* - automaton', 2, { 0: {'a': 0, 'b': 1}, 1: {'c': 1} }, 0, 1),
        valid_strings = ['b', 'ab', 'aab', 'aaaaaaaaaab', 'bc', 'bcc', 'bccccccccccccc', 'abc', 'aabcc', 'aaaaaaaabcccccccc' ],
        invalid_strings = ['3453434', 'a', 'c', 'ac', 'bb', 'abb', 'aaaaccccc', 'abcdf']
      )


def get_test_data():
    return [at1, at2, at3]
