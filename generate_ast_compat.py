from asdl_parse import mk_parser, run_lexer, Tokens
import parser_rts as rts
from typing import List, Tuple
from io import StringIO
import requests

_parse = mk_parser()


def _find_n(s: str, ch, n: int):
    since = 0
    for i in range(0, n - 1):
        since = s.find(ch, since)

    return s[since:s.find(ch, since)]


def parse(text: str, filename: str = "unknown"):
    tokens = list(run_lexer(filename, text))

    res = _parse(None, Tokens(tokens))
    if res[0]:
        return res[1]
    msgs = []
    assert res[1]
    maxline = 0
    for each in res[1]:
        i, msg = each
        token = tokens[i]
        lineno = token.lineno
        maxline = max(lineno, maxline)
        colno = token.colno
        msgs.append(f"Line {lineno + 1}, column {colno}, {msg}")

    e = SyntaxError()
    e.lineno = maxline + 1
    e.msg = '\n'.join(msgs)
    e.filename = filename
    off = token.offset
    e.offset = off
    e.text = text[:text.find('\n', off)]
    raise e


# filename = 'https://raw.githubusercontent.com/python/cpython/master/Parser/Python.asdl'
# text = requests.get(filename).text


def compat_specs(io, specs: List[Tuple[str, List[Tuple[str, str]]]]):
    def l(l):
        io.write(l + '\n')

    l('import ast')
    l('from .make import *')
    l('')

    for typename, fields in specs:
        l(f'class {typename}(metaclass=SupertypeMeta):')
        l(f'    __past__ = ast.{typename}')
        if not fields:
            args = ''
        else:
            args = ''.join(f', {field}=None' for type, field in fields)

        l(f'    def __new__(self{args}):')
        indent = f'        '
        l(f'{indent}"""start checking validation"""')
        for type, field in fields:
            if type == rts.noDefault:
                l(indent +
                  f'if {field} is None: raise ValueError({field + " cannot be None."!r})'
                  )
            elif type == rts.defaultList:
                l(indent + f'if {field} is None: {field} = []')
        l(f'{indent}return ast.{typename}({", ".join(snd for _, snd in fields)})'
          )
        l('')


def compat(python_version: Tuple[int, int], asdl_url: str = None):
    major, minor = python_version
    if asdl_url is None:
        asdl_url = f"https://raw.githubusercontent.com/python/cpython/{major}.{minor}/Parser/Python.asdl"
    text = requests.get(asdl_url).text
    specs = parse(text, asdl_url)
    with open(f'ast_compat/compat{major}k{minor}.py', 'w') as f:
        compat_specs(f, specs)


compat((3, 5))
compat((3, 6))
compat((3, 7))
compat((3, 8))
compat((
    3, 9
), "https://raw.githubusercontent.com/python/cpython/v3.9.0a3/Parser/Python.asdl"
       )