import ast as _ast
from sys import version_info
from numbers import Number


class SupertypeMeta(type):
    def __instancecheck__(self, other):
        return isinstance(other, self.__past__)


if not hasattr(_ast, 'Constant'):

    class Constant(metaclass=SupertypeMeta):
        __past__ = (_ast.Num, _ast.NameConstant, _ast.Str)

        def __new__(cls, i):
            if isinstance(i, Number):
                return _ast.Num(i)

            if isinstance(i, str):
                return _ast.Str(i)

            if isinstance(i, bytes):
                return _ast.Bytes(i)

            if i is None or isinstance(i, bool):
                return _ast.NameConstant(i)

            if isinstance(i, tuple) and version_info < (3, 6):
                return _ast.Tuple(elts=list(map(Constant, i)), ctx=_ast.Load())

    def get_constant(n: Constant):
        if isinstance(n, _ast.Num):
            return n.n
        if isinstance(n, _ast.Str):
            return n.s
        if isinstance(n, _ast.Bytes):
            return n.s
        if isinstance(n, _ast.NameConstant):
            return n.value
        if isinstance(n, _ast.Tuple):
            return tuple(get_constant(each) for each in n.elts)
        raise TypeError(type(n))

else:

    def get_constant(n: _ast.Constant):
        return n.value
