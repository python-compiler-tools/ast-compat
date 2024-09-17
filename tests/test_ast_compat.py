from ast_compat import get_constant
import os
import ast_compat as ast

def test_compat():
    assert get_constant(ast.Constant(0)) == 0
    assert get_constant(ast.Constant((1, 2))) == (1, 2)

    assert ast.unparse(ast.Constant(1)) == '1'
