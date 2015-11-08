from automaton import Automaton
from regexp import *


def remove(regs, k):
    n = len(regs)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if i == k or j == k:
                continue

            regs[i][i] = Add.create(regs[i][i], Concat.create(regs[i][k], KleeneStar.create(regs[k][k]), regs[k][i]))
            regs[j][j] = Add.create(regs[j][j], Concat.create(regs[j][k], KleeneStar.create(regs[k][k]), regs[k][j]))
            regs[i][j] = Add.create(regs[i][j], Concat.create(regs[i][k], KleeneStar.create(regs[k][k]), regs[k][j]))
            regs[j][i] = Add.create(regs[j][i], Concat.create(regs[j][k], KleeneStar.create(regs[k][k]), regs[k][i]))


def build_regexp(automaton):
    states = automaton.states_count()
    regs = [[Empty()] * states for _ in range(states)]

    for i in range(states):
        for j in range(states):
            if i == j:
                regs[i][j] = Eps()

    transitions = automaton.transitions()

    for k1 in transitions.keys():
        for k2 in transitions[k1].keys():
            regs[k1][transitions[k1][k2]] = Symb(k2)

    start = automaton.start()
    finish = automaton.finish()

    for i in range(states):
        if start != i and finish != i:
            remove(regs, i)

    return Concat.create(
                            KleeneStar.create(regs[start][start]),
                            regs[start][finish],
                            KleeneStar(
                                        Add.create(
                                                    Concat.create(
                                                                    regs[finish][start],
                                                                    KleeneStar.create(regs[start][start]),
                                                                    regs[start][finish]
                                                                 ),
                                                    regs[finish][finish]
                                                  )
                                      )
                        )

