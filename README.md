# AST-Compat

backward compatibility library for Python standard library `ast`.

## What is AST-Compat for?

- **backward compatibility for constructing ASTs**
    
    For instance, `ast.arguments` is changed since Python 3.8, that another field `posonlyarg` is introduced,
    hence you should construct an `ast.arguments` with an additional argument `posonlyarg=...` since Python 3.8
    and it wouldn't work if your code is written before Python 3.8.
    
    Through `ast_compat`, you don't have to worry about above question if a new argument is **optional or a list**.
    
    **Note that you should use `ast_compat.XXX` instead of `ast.XXX` to construct ASTs.**
    
- Support **ast.Constant** before Python 3.6.

    `ast.Constant` is convenient, and things like `ast.Num` are redundant according to this observation and improvement: https://bugs.python.org/issue32892
    
    However, `ast.Constant` is not available in 3.5 or earlier versions, thus we backport `ast.Constant` in this library.
    
    To access the content of `ast.Constant` in a compatible way, use `ast_compat.get_constant` instead of `.value`.

- Support dumping AST to string with **ast_compat.unparse**, which synchronizes the tooling code provided by CPython official repo.

## Usage        

```python
import ast_compat as astc
from ast_compat import get_constant

assert get_constant(astc.Constant((1, 2))) == (1, 2)

empty_args = astc.arguments() # work for all of Python 3.5-3.9
```


## Implementation, and rebuild

The compatibility is following the specification of Python ASTs, i.e,
the ADSL file you can find at

`https://github.com/python/cpython/blob/<branch/tag>/Parser/Python.asdl`.

We parse the file, and generate verifications and default argument factories,
check `ast_compat/compat3k*_{ast|unparse}.py`. To explain, `ast_compat/compat3k5_*.py` is for
Python 3.5, and `ast_compat/compat3k9_*.py` is for Python 3.9.

The file of generator is `generate_ast_compat.py`, and the use of generator API is in this way:

```python
from generate_ast_compat import compat
compat((3, 5)) # generate ast_compat/compat3k5_ast.py and  ast_compat/compat3k5_unparse.py
compat((3, 6))
compat((3, 7))
compat((3, 8))
prerelease_url = "https://raw.githubusercontent.com/python/cpython/v3.9.0a3/parser/python.asdl"
compat((3, 9), prerelease_url)
```

The code generation needs Python 3.7+,
though this library works for Python 3.5 and 3.5+.
