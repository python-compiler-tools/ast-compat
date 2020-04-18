from ast import unparsedef unparse(ast_obj):
    IO = io.StringIO()
    Unparser(ast_obj, IO)
    return IO.getvalue().strip()
