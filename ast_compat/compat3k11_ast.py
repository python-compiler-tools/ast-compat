import ast
from .make import *
_unset = object()

class Module(metaclass=SupertypeMeta):
    __past__ = ast.Module
    def __new__(cls, body=_unset, type_ignores=_unset):
        """start checking validation"""
        if body is _unset: body = []
        if type_ignores is _unset: type_ignores = []
        return ast.Module(body, type_ignores)

class Interactive(metaclass=SupertypeMeta):
    __past__ = ast.Interactive
    def __new__(cls, body=_unset):
        """start checking validation"""
        if body is _unset: body = []
        return ast.Interactive(body)

class Expression(metaclass=SupertypeMeta):
    __past__ = ast.Expression
    def __new__(cls, body=_unset):
        """start checking validation"""
        if body is _unset: raise ValueError('body cannot be None.')
        return ast.Expression(body)

class FunctionType(metaclass=SupertypeMeta):
    __past__ = ast.FunctionType
    def __new__(cls, argtypes=_unset, returns=_unset):
        """start checking validation"""
        if argtypes is _unset: argtypes = []
        if returns is _unset: raise ValueError('returns cannot be None.')
        return ast.FunctionType(argtypes, returns)

class FunctionDef(metaclass=SupertypeMeta):
    __past__ = ast.FunctionDef
    def __new__(cls, name=_unset, args=_unset, body=_unset, decorator_list=_unset, returns=_unset, type_comment=_unset):
        """start checking validation"""
        if name is _unset: raise ValueError('name cannot be None.')
        if args is _unset: raise ValueError('args cannot be None.')
        if body is _unset: body = []
        if decorator_list is _unset: decorator_list = []
        if returns is _unset: returns = None
        if type_comment is _unset: type_comment = None
        return ast.FunctionDef(name, args, body, decorator_list, returns, type_comment)

class AsyncFunctionDef(metaclass=SupertypeMeta):
    __past__ = ast.AsyncFunctionDef
    def __new__(cls, name=_unset, args=_unset, body=_unset, decorator_list=_unset, returns=_unset, type_comment=_unset):
        """start checking validation"""
        if name is _unset: raise ValueError('name cannot be None.')
        if args is _unset: raise ValueError('args cannot be None.')
        if body is _unset: body = []
        if decorator_list is _unset: decorator_list = []
        if returns is _unset: returns = None
        if type_comment is _unset: type_comment = None
        return ast.AsyncFunctionDef(name, args, body, decorator_list, returns, type_comment)

class ClassDef(metaclass=SupertypeMeta):
    __past__ = ast.ClassDef
    def __new__(cls, name=_unset, bases=_unset, keywords=_unset, body=_unset, decorator_list=_unset):
        """start checking validation"""
        if name is _unset: raise ValueError('name cannot be None.')
        if bases is _unset: bases = []
        if keywords is _unset: keywords = []
        if body is _unset: body = []
        if decorator_list is _unset: decorator_list = []
        return ast.ClassDef(name, bases, keywords, body, decorator_list)

class Return(metaclass=SupertypeMeta):
    __past__ = ast.Return
    def __new__(cls, value=_unset):
        """start checking validation"""
        if value is _unset: value = None
        return ast.Return(value)

class Delete(metaclass=SupertypeMeta):
    __past__ = ast.Delete
    def __new__(cls, targets=_unset):
        """start checking validation"""
        if targets is _unset: targets = []
        return ast.Delete(targets)

class Assign(metaclass=SupertypeMeta):
    __past__ = ast.Assign
    def __new__(cls, targets=_unset, value=_unset, type_comment=_unset):
        """start checking validation"""
        if targets is _unset: targets = []
        if value is _unset: raise ValueError('value cannot be None.')
        if type_comment is _unset: type_comment = None
        return ast.Assign(targets, value, type_comment)

class AugAssign(metaclass=SupertypeMeta):
    __past__ = ast.AugAssign
    def __new__(cls, target=_unset, op=_unset, value=_unset):
        """start checking validation"""
        if target is _unset: raise ValueError('target cannot be None.')
        if op is _unset: raise ValueError('op cannot be None.')
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.AugAssign(target, op, value)

class AnnAssign(metaclass=SupertypeMeta):
    __past__ = ast.AnnAssign
    def __new__(cls, target=_unset, annotation=_unset, value=_unset, simple=_unset):
        """start checking validation"""
        if target is _unset: raise ValueError('target cannot be None.')
        if annotation is _unset: raise ValueError('annotation cannot be None.')
        if value is _unset: value = None
        if simple is _unset: raise ValueError('simple cannot be None.')
        return ast.AnnAssign(target, annotation, value, simple)

class For(metaclass=SupertypeMeta):
    __past__ = ast.For
    def __new__(cls, target=_unset, iter=_unset, body=_unset, orelse=_unset, type_comment=_unset):
        """start checking validation"""
        if target is _unset: raise ValueError('target cannot be None.')
        if iter is _unset: raise ValueError('iter cannot be None.')
        if body is _unset: body = []
        if orelse is _unset: orelse = []
        if type_comment is _unset: type_comment = None
        return ast.For(target, iter, body, orelse, type_comment)

class AsyncFor(metaclass=SupertypeMeta):
    __past__ = ast.AsyncFor
    def __new__(cls, target=_unset, iter=_unset, body=_unset, orelse=_unset, type_comment=_unset):
        """start checking validation"""
        if target is _unset: raise ValueError('target cannot be None.')
        if iter is _unset: raise ValueError('iter cannot be None.')
        if body is _unset: body = []
        if orelse is _unset: orelse = []
        if type_comment is _unset: type_comment = None
        return ast.AsyncFor(target, iter, body, orelse, type_comment)

class While(metaclass=SupertypeMeta):
    __past__ = ast.While
    def __new__(cls, test=_unset, body=_unset, orelse=_unset):
        """start checking validation"""
        if test is _unset: raise ValueError('test cannot be None.')
        if body is _unset: body = []
        if orelse is _unset: orelse = []
        return ast.While(test, body, orelse)

class If(metaclass=SupertypeMeta):
    __past__ = ast.If
    def __new__(cls, test=_unset, body=_unset, orelse=_unset):
        """start checking validation"""
        if test is _unset: raise ValueError('test cannot be None.')
        if body is _unset: body = []
        if orelse is _unset: orelse = []
        return ast.If(test, body, orelse)

class With(metaclass=SupertypeMeta):
    __past__ = ast.With
    def __new__(cls, items=_unset, body=_unset, type_comment=_unset):
        """start checking validation"""
        if items is _unset: items = []
        if body is _unset: body = []
        if type_comment is _unset: type_comment = None
        return ast.With(items, body, type_comment)

class AsyncWith(metaclass=SupertypeMeta):
    __past__ = ast.AsyncWith
    def __new__(cls, items=_unset, body=_unset, type_comment=_unset):
        """start checking validation"""
        if items is _unset: items = []
        if body is _unset: body = []
        if type_comment is _unset: type_comment = None
        return ast.AsyncWith(items, body, type_comment)

class Match(metaclass=SupertypeMeta):
    __past__ = ast.Match
    def __new__(cls, subject=_unset, cases=_unset):
        """start checking validation"""
        if subject is _unset: raise ValueError('subject cannot be None.')
        if cases is _unset: cases = []
        return ast.Match(subject, cases)

class Raise(metaclass=SupertypeMeta):
    __past__ = ast.Raise
    def __new__(cls, exc=_unset, cause=_unset):
        """start checking validation"""
        if exc is _unset: exc = None
        if cause is _unset: cause = None
        return ast.Raise(exc, cause)

class Try(metaclass=SupertypeMeta):
    __past__ = ast.Try
    def __new__(cls, body=_unset, handlers=_unset, orelse=_unset, finalbody=_unset):
        """start checking validation"""
        if body is _unset: body = []
        if handlers is _unset: handlers = []
        if orelse is _unset: orelse = []
        if finalbody is _unset: finalbody = []
        return ast.Try(body, handlers, orelse, finalbody)

class TryStar(metaclass=SupertypeMeta):
    __past__ = ast.TryStar
    def __new__(cls, body=_unset, handlers=_unset, orelse=_unset, finalbody=_unset):
        """start checking validation"""
        if body is _unset: body = []
        if handlers is _unset: handlers = []
        if orelse is _unset: orelse = []
        if finalbody is _unset: finalbody = []
        return ast.TryStar(body, handlers, orelse, finalbody)

class Assert(metaclass=SupertypeMeta):
    __past__ = ast.Assert
    def __new__(cls, test=_unset, msg=_unset):
        """start checking validation"""
        if test is _unset: raise ValueError('test cannot be None.')
        if msg is _unset: msg = None
        return ast.Assert(test, msg)

class Import(metaclass=SupertypeMeta):
    __past__ = ast.Import
    def __new__(cls, names=_unset):
        """start checking validation"""
        if names is _unset: names = []
        return ast.Import(names)

class ImportFrom(metaclass=SupertypeMeta):
    __past__ = ast.ImportFrom
    def __new__(cls, module=_unset, names=_unset, level=_unset):
        """start checking validation"""
        if module is _unset: module = None
        if names is _unset: names = []
        if level is _unset: level = None
        return ast.ImportFrom(module, names, level)

class Global(metaclass=SupertypeMeta):
    __past__ = ast.Global
    def __new__(cls, names=_unset):
        """start checking validation"""
        if names is _unset: names = []
        return ast.Global(names)

class Nonlocal(metaclass=SupertypeMeta):
    __past__ = ast.Nonlocal
    def __new__(cls, names=_unset):
        """start checking validation"""
        if names is _unset: names = []
        return ast.Nonlocal(names)

class Expr(metaclass=SupertypeMeta):
    __past__ = ast.Expr
    def __new__(cls, value=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.Expr(value)

class Pass(metaclass=SupertypeMeta):
    __past__ = ast.Pass
    def __new__(cls):
        """start checking validation"""
        return ast.Pass()

class Break(metaclass=SupertypeMeta):
    __past__ = ast.Break
    def __new__(cls):
        """start checking validation"""
        return ast.Break()

class Continue(metaclass=SupertypeMeta):
    __past__ = ast.Continue
    def __new__(cls):
        """start checking validation"""
        return ast.Continue()

class BoolOp(metaclass=SupertypeMeta):
    __past__ = ast.BoolOp
    def __new__(cls, op=_unset, values=_unset):
        """start checking validation"""
        if op is _unset: raise ValueError('op cannot be None.')
        if values is _unset: values = []
        return ast.BoolOp(op, values)

class NamedExpr(metaclass=SupertypeMeta):
    __past__ = ast.NamedExpr
    def __new__(cls, target=_unset, value=_unset):
        """start checking validation"""
        if target is _unset: raise ValueError('target cannot be None.')
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.NamedExpr(target, value)

class BinOp(metaclass=SupertypeMeta):
    __past__ = ast.BinOp
    def __new__(cls, left=_unset, op=_unset, right=_unset):
        """start checking validation"""
        if left is _unset: raise ValueError('left cannot be None.')
        if op is _unset: raise ValueError('op cannot be None.')
        if right is _unset: raise ValueError('right cannot be None.')
        return ast.BinOp(left, op, right)

class UnaryOp(metaclass=SupertypeMeta):
    __past__ = ast.UnaryOp
    def __new__(cls, op=_unset, operand=_unset):
        """start checking validation"""
        if op is _unset: raise ValueError('op cannot be None.')
        if operand is _unset: raise ValueError('operand cannot be None.')
        return ast.UnaryOp(op, operand)

class Lambda(metaclass=SupertypeMeta):
    __past__ = ast.Lambda
    def __new__(cls, args=_unset, body=_unset):
        """start checking validation"""
        if args is _unset: raise ValueError('args cannot be None.')
        if body is _unset: raise ValueError('body cannot be None.')
        return ast.Lambda(args, body)

class IfExp(metaclass=SupertypeMeta):
    __past__ = ast.IfExp
    def __new__(cls, test=_unset, body=_unset, orelse=_unset):
        """start checking validation"""
        if test is _unset: raise ValueError('test cannot be None.')
        if body is _unset: raise ValueError('body cannot be None.')
        if orelse is _unset: raise ValueError('orelse cannot be None.')
        return ast.IfExp(test, body, orelse)

class Dict(metaclass=SupertypeMeta):
    __past__ = ast.Dict
    def __new__(cls, keys=_unset, values=_unset):
        """start checking validation"""
        if keys is _unset: keys = []
        if values is _unset: values = []
        return ast.Dict(keys, values)

class Set(metaclass=SupertypeMeta):
    __past__ = ast.Set
    def __new__(cls, elts=_unset):
        """start checking validation"""
        if elts is _unset: elts = []
        return ast.Set(elts)

class ListComp(metaclass=SupertypeMeta):
    __past__ = ast.ListComp
    def __new__(cls, elt=_unset, generators=_unset):
        """start checking validation"""
        if elt is _unset: raise ValueError('elt cannot be None.')
        if generators is _unset: generators = []
        return ast.ListComp(elt, generators)

class SetComp(metaclass=SupertypeMeta):
    __past__ = ast.SetComp
    def __new__(cls, elt=_unset, generators=_unset):
        """start checking validation"""
        if elt is _unset: raise ValueError('elt cannot be None.')
        if generators is _unset: generators = []
        return ast.SetComp(elt, generators)

class DictComp(metaclass=SupertypeMeta):
    __past__ = ast.DictComp
    def __new__(cls, key=_unset, value=_unset, generators=_unset):
        """start checking validation"""
        if key is _unset: raise ValueError('key cannot be None.')
        if value is _unset: raise ValueError('value cannot be None.')
        if generators is _unset: generators = []
        return ast.DictComp(key, value, generators)

class GeneratorExp(metaclass=SupertypeMeta):
    __past__ = ast.GeneratorExp
    def __new__(cls, elt=_unset, generators=_unset):
        """start checking validation"""
        if elt is _unset: raise ValueError('elt cannot be None.')
        if generators is _unset: generators = []
        return ast.GeneratorExp(elt, generators)

class Await(metaclass=SupertypeMeta):
    __past__ = ast.Await
    def __new__(cls, value=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.Await(value)

class Yield(metaclass=SupertypeMeta):
    __past__ = ast.Yield
    def __new__(cls, value=_unset):
        """start checking validation"""
        if value is _unset: value = None
        return ast.Yield(value)

class YieldFrom(metaclass=SupertypeMeta):
    __past__ = ast.YieldFrom
    def __new__(cls, value=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.YieldFrom(value)

class Compare(metaclass=SupertypeMeta):
    __past__ = ast.Compare
    def __new__(cls, left=_unset, ops=_unset, comparators=_unset):
        """start checking validation"""
        if left is _unset: raise ValueError('left cannot be None.')
        if ops is _unset: ops = []
        if comparators is _unset: comparators = []
        return ast.Compare(left, ops, comparators)

class Call(metaclass=SupertypeMeta):
    __past__ = ast.Call
    def __new__(cls, func=_unset, args=_unset, keywords=_unset):
        """start checking validation"""
        if func is _unset: raise ValueError('func cannot be None.')
        if args is _unset: args = []
        if keywords is _unset: keywords = []
        return ast.Call(func, args, keywords)

class FormattedValue(metaclass=SupertypeMeta):
    __past__ = ast.FormattedValue
    def __new__(cls, value=_unset, conversion=_unset, format_spec=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        if conversion is _unset: raise ValueError('conversion cannot be None.')
        if format_spec is _unset: format_spec = None
        return ast.FormattedValue(value, conversion, format_spec)

class JoinedStr(metaclass=SupertypeMeta):
    __past__ = ast.JoinedStr
    def __new__(cls, values=_unset):
        """start checking validation"""
        if values is _unset: values = []
        return ast.JoinedStr(values)

class Constant(metaclass=SupertypeMeta):
    __past__ = ast.Constant
    def __new__(cls, value=_unset, kind=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        if kind is _unset: kind = None
        return ast.Constant(value, kind)

class Attribute(metaclass=SupertypeMeta):
    __past__ = ast.Attribute
    def __new__(cls, value=_unset, attr=_unset, ctx=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        if attr is _unset: raise ValueError('attr cannot be None.')
        if ctx is _unset: raise ValueError('ctx cannot be None.')
        return ast.Attribute(value, attr, ctx)

class Subscript(metaclass=SupertypeMeta):
    __past__ = ast.Subscript
    def __new__(cls, value=_unset, slice=_unset, ctx=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        if slice is _unset: raise ValueError('slice cannot be None.')
        if ctx is _unset: raise ValueError('ctx cannot be None.')
        return ast.Subscript(value, slice, ctx)

class Starred(metaclass=SupertypeMeta):
    __past__ = ast.Starred
    def __new__(cls, value=_unset, ctx=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        if ctx is _unset: raise ValueError('ctx cannot be None.')
        return ast.Starred(value, ctx)

class Name(metaclass=SupertypeMeta):
    __past__ = ast.Name
    def __new__(cls, id=_unset, ctx=_unset):
        """start checking validation"""
        if id is _unset: raise ValueError('id cannot be None.')
        if ctx is _unset: raise ValueError('ctx cannot be None.')
        return ast.Name(id, ctx)

class List(metaclass=SupertypeMeta):
    __past__ = ast.List
    def __new__(cls, elts=_unset, ctx=_unset):
        """start checking validation"""
        if elts is _unset: elts = []
        if ctx is _unset: raise ValueError('ctx cannot be None.')
        return ast.List(elts, ctx)

class Tuple(metaclass=SupertypeMeta):
    __past__ = ast.Tuple
    def __new__(cls, elts=_unset, ctx=_unset):
        """start checking validation"""
        if elts is _unset: elts = []
        if ctx is _unset: raise ValueError('ctx cannot be None.')
        return ast.Tuple(elts, ctx)

class Slice(metaclass=SupertypeMeta):
    __past__ = ast.Slice
    def __new__(cls, lower=_unset, upper=_unset, step=_unset):
        """start checking validation"""
        if lower is _unset: lower = None
        if upper is _unset: upper = None
        if step is _unset: step = None
        return ast.Slice(lower, upper, step)

class Load(metaclass=SupertypeMeta):
    __past__ = ast.Load
    def __new__(cls):
        """start checking validation"""
        return ast.Load()

class Store(metaclass=SupertypeMeta):
    __past__ = ast.Store
    def __new__(cls):
        """start checking validation"""
        return ast.Store()

class Del(metaclass=SupertypeMeta):
    __past__ = ast.Del
    def __new__(cls):
        """start checking validation"""
        return ast.Del()

class And(metaclass=SupertypeMeta):
    __past__ = ast.And
    def __new__(cls):
        """start checking validation"""
        return ast.And()

class Or(metaclass=SupertypeMeta):
    __past__ = ast.Or
    def __new__(cls):
        """start checking validation"""
        return ast.Or()

class Add(metaclass=SupertypeMeta):
    __past__ = ast.Add
    def __new__(cls):
        """start checking validation"""
        return ast.Add()

class Sub(metaclass=SupertypeMeta):
    __past__ = ast.Sub
    def __new__(cls):
        """start checking validation"""
        return ast.Sub()

class Mult(metaclass=SupertypeMeta):
    __past__ = ast.Mult
    def __new__(cls):
        """start checking validation"""
        return ast.Mult()

class MatMult(metaclass=SupertypeMeta):
    __past__ = ast.MatMult
    def __new__(cls):
        """start checking validation"""
        return ast.MatMult()

class Div(metaclass=SupertypeMeta):
    __past__ = ast.Div
    def __new__(cls):
        """start checking validation"""
        return ast.Div()

class Mod(metaclass=SupertypeMeta):
    __past__ = ast.Mod
    def __new__(cls):
        """start checking validation"""
        return ast.Mod()

class Pow(metaclass=SupertypeMeta):
    __past__ = ast.Pow
    def __new__(cls):
        """start checking validation"""
        return ast.Pow()

class LShift(metaclass=SupertypeMeta):
    __past__ = ast.LShift
    def __new__(cls):
        """start checking validation"""
        return ast.LShift()

class RShift(metaclass=SupertypeMeta):
    __past__ = ast.RShift
    def __new__(cls):
        """start checking validation"""
        return ast.RShift()

class BitOr(metaclass=SupertypeMeta):
    __past__ = ast.BitOr
    def __new__(cls):
        """start checking validation"""
        return ast.BitOr()

class BitXor(metaclass=SupertypeMeta):
    __past__ = ast.BitXor
    def __new__(cls):
        """start checking validation"""
        return ast.BitXor()

class BitAnd(metaclass=SupertypeMeta):
    __past__ = ast.BitAnd
    def __new__(cls):
        """start checking validation"""
        return ast.BitAnd()

class FloorDiv(metaclass=SupertypeMeta):
    __past__ = ast.FloorDiv
    def __new__(cls):
        """start checking validation"""
        return ast.FloorDiv()

class Invert(metaclass=SupertypeMeta):
    __past__ = ast.Invert
    def __new__(cls):
        """start checking validation"""
        return ast.Invert()

class Not(metaclass=SupertypeMeta):
    __past__ = ast.Not
    def __new__(cls):
        """start checking validation"""
        return ast.Not()

class UAdd(metaclass=SupertypeMeta):
    __past__ = ast.UAdd
    def __new__(cls):
        """start checking validation"""
        return ast.UAdd()

class USub(metaclass=SupertypeMeta):
    __past__ = ast.USub
    def __new__(cls):
        """start checking validation"""
        return ast.USub()

class Eq(metaclass=SupertypeMeta):
    __past__ = ast.Eq
    def __new__(cls):
        """start checking validation"""
        return ast.Eq()

class NotEq(metaclass=SupertypeMeta):
    __past__ = ast.NotEq
    def __new__(cls):
        """start checking validation"""
        return ast.NotEq()

class Lt(metaclass=SupertypeMeta):
    __past__ = ast.Lt
    def __new__(cls):
        """start checking validation"""
        return ast.Lt()

class LtE(metaclass=SupertypeMeta):
    __past__ = ast.LtE
    def __new__(cls):
        """start checking validation"""
        return ast.LtE()

class Gt(metaclass=SupertypeMeta):
    __past__ = ast.Gt
    def __new__(cls):
        """start checking validation"""
        return ast.Gt()

class GtE(metaclass=SupertypeMeta):
    __past__ = ast.GtE
    def __new__(cls):
        """start checking validation"""
        return ast.GtE()

class Is(metaclass=SupertypeMeta):
    __past__ = ast.Is
    def __new__(cls):
        """start checking validation"""
        return ast.Is()

class IsNot(metaclass=SupertypeMeta):
    __past__ = ast.IsNot
    def __new__(cls):
        """start checking validation"""
        return ast.IsNot()

class In(metaclass=SupertypeMeta):
    __past__ = ast.In
    def __new__(cls):
        """start checking validation"""
        return ast.In()

class NotIn(metaclass=SupertypeMeta):
    __past__ = ast.NotIn
    def __new__(cls):
        """start checking validation"""
        return ast.NotIn()

class comprehension(metaclass=SupertypeMeta):
    __past__ = ast.comprehension
    def __new__(cls, target=_unset, iter=_unset, ifs=_unset, is_async=_unset):
        """start checking validation"""
        if target is _unset: raise ValueError('target cannot be None.')
        if iter is _unset: raise ValueError('iter cannot be None.')
        if ifs is _unset: ifs = []
        if is_async is _unset: raise ValueError('is_async cannot be None.')
        return ast.comprehension(target, iter, ifs, is_async)

class ExceptHandler(metaclass=SupertypeMeta):
    __past__ = ast.ExceptHandler
    def __new__(cls, type=_unset, name=_unset, body=_unset):
        """start checking validation"""
        if type is _unset: type = None
        if name is _unset: name = None
        if body is _unset: body = []
        return ast.ExceptHandler(type, name, body)

class arguments(metaclass=SupertypeMeta):
    __past__ = ast.arguments
    def __new__(cls, posonlyargs=_unset, args=_unset, vararg=_unset, kwonlyargs=_unset, kw_defaults=_unset, kwarg=_unset, defaults=_unset):
        """start checking validation"""
        if posonlyargs is _unset: posonlyargs = []
        if args is _unset: args = []
        if vararg is _unset: vararg = None
        if kwonlyargs is _unset: kwonlyargs = []
        if kw_defaults is _unset: kw_defaults = []
        if kwarg is _unset: kwarg = None
        if defaults is _unset: defaults = []
        return ast.arguments(posonlyargs, args, vararg, kwonlyargs, kw_defaults, kwarg, defaults)

class arg(metaclass=SupertypeMeta):
    __past__ = ast.arg
    def __new__(cls, arg=_unset, annotation=_unset, type_comment=_unset):
        """start checking validation"""
        if arg is _unset: raise ValueError('arg cannot be None.')
        if annotation is _unset: annotation = None
        if type_comment is _unset: type_comment = None
        return ast.arg(arg, annotation, type_comment)

class keyword(metaclass=SupertypeMeta):
    __past__ = ast.keyword
    def __new__(cls, arg=_unset, value=_unset):
        """start checking validation"""
        if arg is _unset: arg = None
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.keyword(arg, value)

class alias(metaclass=SupertypeMeta):
    __past__ = ast.alias
    def __new__(cls, name=_unset, asname=_unset):
        """start checking validation"""
        if name is _unset: raise ValueError('name cannot be None.')
        if asname is _unset: asname = None
        return ast.alias(name, asname)

class withitem(metaclass=SupertypeMeta):
    __past__ = ast.withitem
    def __new__(cls, context_expr=_unset, optional_vars=_unset):
        """start checking validation"""
        if context_expr is _unset: raise ValueError('context_expr cannot be None.')
        if optional_vars is _unset: optional_vars = None
        return ast.withitem(context_expr, optional_vars)

class match_case(metaclass=SupertypeMeta):
    __past__ = ast.match_case
    def __new__(cls, pattern=_unset, guard=_unset, body=_unset):
        """start checking validation"""
        if pattern is _unset: raise ValueError('pattern cannot be None.')
        if guard is _unset: guard = None
        if body is _unset: body = []
        return ast.match_case(pattern, guard, body)

class MatchValue(metaclass=SupertypeMeta):
    __past__ = ast.MatchValue
    def __new__(cls, value=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.MatchValue(value)

class MatchSingleton(metaclass=SupertypeMeta):
    __past__ = ast.MatchSingleton
    def __new__(cls, value=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.MatchSingleton(value)

class MatchSequence(metaclass=SupertypeMeta):
    __past__ = ast.MatchSequence
    def __new__(cls, patterns=_unset):
        """start checking validation"""
        if patterns is _unset: patterns = []
        return ast.MatchSequence(patterns)

class MatchMapping(metaclass=SupertypeMeta):
    __past__ = ast.MatchMapping
    def __new__(cls, keys=_unset, patterns=_unset, rest=_unset):
        """start checking validation"""
        if keys is _unset: keys = []
        if patterns is _unset: patterns = []
        if rest is _unset: rest = None
        return ast.MatchMapping(keys, patterns, rest)

class MatchClass(metaclass=SupertypeMeta):
    __past__ = ast.MatchClass
    def __new__(cls, cls=_unset, patterns=_unset, kwd_attrs=_unset, kwd_patterns=_unset):
        """start checking validation"""
        if cls is _unset: raise ValueError('cls cannot be None.')
        if patterns is _unset: patterns = []
        if kwd_attrs is _unset: kwd_attrs = []
        if kwd_patterns is _unset: kwd_patterns = []
        return ast.MatchClass(cls, patterns, kwd_attrs, kwd_patterns)

class MatchStar(metaclass=SupertypeMeta):
    __past__ = ast.MatchStar
    def __new__(cls, name=_unset):
        """start checking validation"""
        if name is _unset: name = None
        return ast.MatchStar(name)

class MatchAs(metaclass=SupertypeMeta):
    __past__ = ast.MatchAs
    def __new__(cls, pattern=_unset, name=_unset):
        """start checking validation"""
        if pattern is _unset: pattern = None
        if name is _unset: name = None
        return ast.MatchAs(pattern, name)

class MatchOr(metaclass=SupertypeMeta):
    __past__ = ast.MatchOr
    def __new__(cls, patterns=_unset):
        """start checking validation"""
        if patterns is _unset: patterns = []
        return ast.MatchOr(patterns)

class TypeIgnore(metaclass=SupertypeMeta):
    __past__ = ast.TypeIgnore
    def __new__(cls, lineno=_unset, tag=_unset):
        """start checking validation"""
        if lineno is _unset: raise ValueError('lineno cannot be None.')
        if tag is _unset: raise ValueError('tag cannot be None.')
        return ast.TypeIgnore(lineno, tag)

