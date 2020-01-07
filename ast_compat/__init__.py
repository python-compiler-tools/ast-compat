import ast_compat.make as _make
from ast_compat.make import get_constant

__version__ = '0.1.0'

_g = globals()
for k, v in _make.ast.__dict__.items():
    if not k.startswith('__'):
        _g[k] = v
del _g, _make
