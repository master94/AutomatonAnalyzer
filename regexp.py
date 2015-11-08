class RegBase:
    pass


class Eps(RegBase):
    def __repr__(self):
        return 'eps'


class Empty(RegBase):
    def __repr__(self):
        return '0'


class KleeneStar(RegBase):
    def __init__(self, reg):
        self.__reg = reg

    def __repr__(self):
        s = str(self.__reg)
        if len(s) > 1 and s[0] + s[-1] != '()':
            s = '(' + s + ')'
        return s + '*'

    @staticmethod
    def create(expr):
        if isinstance(expr, Eps):
            return Eps()
        elif isinstance(expr, Empty):
            return Empty()
        elif isinstance(expr, KleeneStar):
            return expr
        elif isinstance(expr, Add):
            expr = remove_eps(expr)

        return KleeneStar(expr)


class Concat(RegBase):
    def __init__(self, exp1, exp2, *exprs):
        self.__exprs = [exp1, exp2] + list(*exprs)

    def __repr__(self):
        return ''.join(map(str, self.__exprs))

    @staticmethod
    def create(exp1, exp2, *rest):
        exprs = [exp1, exp2] + list(rest)
        if any(map(lambda e: isinstance(e, Empty), exprs)):
            return Empty()

        exprs = list(filter(lambda e: not isinstance(e, Eps), exprs))
        if len(exprs) == 0:
            return Eps()
        elif len(exprs) == 1:
            return exprs[0]

        return Concat(exprs[0], exprs[1], exprs[2:])


class Add(RegBase):
    def __init__(self, exp1, exp2, *exprs):
        self.__exprs = [exp1, exp2] + list(*exprs)

    def __repr__(self):
        return '(' + ' + '.join(map(str, self.__exprs)) + ')'

    def exprs(self):
        return self.__exprs

    @staticmethod
    def create(exp1, exp2, *rest):
        exprs = [exp1, exp2] + list(rest)

        exprs = list(set(filter(lambda e: not isinstance(e, Empty), exprs)))
        if len(exprs) == 0:
            return Empty()
        elif len(exprs) == 1:
            return exprs[0]

        return Add(exp1, exp2, rest)

    @staticmethod
    def remove_eps(add):
        if not isinstance(add, Add):
            return add

        exprs = list(map(remove_eps, filter(lambda e: not isinstance(e, Eps), add.exprs())))
        if len(exprs) == 0:
            return Eps()
        elif len(exprs) == 1:
            return exprs[0]

        return Add(exprs[0], exprs[1], exprs[2:])


class Symb(RegBase):
    def __init__(self, symb):
        self.__symb = symb

    def __repr__(self):
        return self.__symb
