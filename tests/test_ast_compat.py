from ast_compat import get_constant
import ast_compat as ast

assert get_constant(ast.Constant(0)) == 0
assert get_constant(ast.Constant((1, 2))) == (1, 2)

print(repr(ast.unparse(ast.Constant(1))))