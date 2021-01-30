from sys import version_info

ver = version_info[:2]
if ver == (3, 5):
    from .compat3k5_ast import *
    from .compat3k5_unparse import unparse

elif ver == (3, 6):
    from .compat3k6_ast import *
    from .compat3k6_unparse import unparse

elif ver == (3, 7):
    from .compat3k7_ast import *
    from .compat3k7_unparse import unparse

elif ver == (3, 8):
    from .compat3k8_ast import *
    from .compat3k8_unparse import unparse

elif ver == (3, 9):
    from .compat3k9_ast import *
    from .compat3k9_unparse import unparse
