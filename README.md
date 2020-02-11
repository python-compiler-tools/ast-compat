# AST-Compat

backward compatibility library for Python standard library `ast`.

## What is AST-Compat for?

- **backward compatibility for constructing ASTs**
    
    For instance, `ast.arguments` is changed since Python 3.8, that another field `posonlyarg` is introduced,
    hence you should construct an `ast.arguments` with an additional argument `posonlyarg=...` since Python 3.8
    and it wouldn't work if your code is written before Python 3.8.
    
    Through `ast_compat`, you don't have to worry about above question if the new arguments are **optional or a list**.
    
- Supporting **ast.Constant** before Python 3.6.

    `ast.Constant` is convenient, and things like `ast.Num` are redundant according to this observation and improvement: https://bugs.python.org/issue32892
    
    However, `ast.Constant` is not available in 3.5 or earlier versions, thus we backport `ast.Constant` in this library.
    
    To access the content of `ast.Constant` in a compatible way, use `ast_compat.get_constant` instead of `.value`.
        
```python
import ast_compat as ast
from ast_compat import get_constant

assert get_constant(ast.Constant((1, 2))) == (1, 2)
```