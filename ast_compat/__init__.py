from sys import version_info

ver = version_info[:2]
if ver == (3, 5):
    from .compat3k5 import *

elif ver == (3, 6):
    from .compat3k6 import *

elif ver == (3, 7):
    from .compat3k6 import *

elif ver == (3, 8):
    from .compat3k6 import *

elif ver == (3, 9):
    from .compat3k6 import *
