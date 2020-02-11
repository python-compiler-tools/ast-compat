from typing import Generic, TypeVar
T = TypeVar('T')

__all__ = [
    'prim__mk__ast', 'prim__cons', 'prim__nil', 'Tokens', 'defaultList',
    'defaultNone', 'noDefault'
]

defaultList = 'defaultList'

defaultNone = 'defaultNone'

noDefault = 'noDefault'


class Tokens:
    __slots__ = ['array', 'offset']

    def __init__(self, array):
        self.array = array
        self.offset = 0

    def __repr__(self):
        from prettyprinter import pformat
        return pformat(self)


class State:
    def __init__(self):
        pass


class AST(Generic[T]):
    __slots__ = ['tag', "contents"]

    def __init__(self, tag: str, contents: T):
        self.tag = tag
        self.contents = contents

    def __repr__(self):
        from prettyprinter import pformat
        return pformat(self)


class Nil:
    nil = None
    __slots__ = []

    def __init__(self):
        if Nil.nil is None:
            Nil.nil = self
            return
        raise ValueError("Nil cannot get instantiated twice.")

    def __len__(self):
        return 0

    def __getitem__(self, n):
        raise IndexError('Out of bounds')

    @property
    def head(self):
        raise IndexError('Out of bounds')

    @property
    def tail(self):
        raise IndexError('Out of bounds')

    def __repr__(self):
        return "[]"


_nil = Nil()


class Cons:
    __slots__ = ['head', 'tail']

    def __init__(self, _head, _tail):
        self.head = _head
        self.tail = _tail

    def __len__(self):
        nil = _nil
        l = 0
        while self is not nil:
            l += 1
            # noinspection PyMethodFirstArgAssignment
            self = self.tail
        return l

    def __iter__(self):
        nil = _nil
        while self is not nil:
            yield self.head
            # noinspection PyMethodFirstArgAssignment
            self = self.tail

    def __getitem__(self, n):
        while n != 0:
            # noinspection PyMethodFirstArgAssignment
            self = self.tail
            n -= 1
        return self.head

    def __repr__(self):
        return repr(list(self))


prim__mk__ast = AST
prim__cons = Cons
prim__nil = _nil
