# AST-Compat

Cross-version Python ast library.

```python
import ast_compat as ast
from ast_compat import get_constant

assert get_constant(ast.Constant(0)) == 0
```