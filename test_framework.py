import re

from termcolor import cprint, colored

from analysis import build_regexp
from automaton import Automaton

prefered_console_width = 80


def run_tests(tests):
    for test in tests:
        run_test(test.automaton, test.valid_strings, test.invalid_strings)
        print('\n' + ('=' * prefered_console_width) + '\n')


def run_test(automaton, valid_strings, invalid_strings):
    cprint('Automaton "{0}"'.format(automaton.name()), 'red', attrs=['bold'])

    string_acceptance_test('Valid string test:', valid_strings, automaton.accepts)
    string_acceptance_test('Invalid strings test:', invalid_strings, lambda s: not automaton.accepts(s))
   
    regexp = build_regexp(automaton)
    
    try:
        regexp_str = '^' + str(regexp).replace('+', '|') + '$'
        python_regexp = re.compile(regexp_str)
    except re.error as e:
        print('Cannot compile regexp {0}'.format(str(regexp)))
        return

    cprint('Regular expression "{0}"'.format(str(regexp)), 'red', attrs=['bold'])
    string_acceptance_test('Valid strings test:', valid_strings, python_regexp.match)
    string_acceptance_test('Invalid strings test:', invalid_strings, lambda s: not python_regexp.match(s))


def string_acceptance_test(header, strings, accept_func):
    cprint(header, 'yellow')

    for s in strings:
        status = ('OK', 'green') if accept_func(s) else ('FAIL', 'red')
        status_str = colored(status[0], status[1])

        max_word_len = int(prefered_console_width * 0.9)
        word = '"' + s[:min(max_word_len, len(s))] + '"'
        
        spaces_count = prefered_console_width - len(word) - len(status[0])
        print(word + (' ' * spaces_count) + status_str)
