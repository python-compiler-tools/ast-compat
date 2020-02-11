import ast
from .make import *

class Module(metaclass=SupertypeMeta):
    __past__ = ast.Module
    def __new__(self, body=None):
        """start checking validation"""
        if body is None: body = []
        return ast.Module(body)

class Interactive(metaclass=SupertypeMeta):
    __past__ = ast.Interactive
    def __new__(self, body=None):
        """start checking validation"""
        if body is None: body = []
        return ast.Interactive(body)

class Expression(metaclass=SupertypeMeta):
    __past__ = ast.Expression
    def __new__(self, body=None):
        """start checking validation"""
        if body is None: raise ValueError('body cannot be None.')
        return ast.Expression(body)

class Suite(metaclass=SupertypeMeta):
    __past__ = ast.Suite
    def __new__(self, body=None):
        """start checking validation"""
        if body is None: body = []
        return ast.Suite(body)

class FunctionDef(metaclass=SupertypeMeta):
    __past__ = ast.FunctionDef
    def __new__(self, name=None, args=None, body=None, decorator_list=None, returns=None):
        """start checking validation"""
        if name is None: raise ValueError('name cannot be None.')
        if args is None: raise ValueError('args cannot be None.')
        if body is None: body = []
        if decorator_list is None: decorator_list = []
        return ast.FunctionDef(name, args, body, decorator_list, returns)

class AsyncFunctionDef(metaclass=SupertypeMeta):
    __past__ = ast.AsyncFunctionDef
    def __new__(self, name=None, args=None, body=None, decorator_list=None, returns=None):
        """start checking validation"""
        if name is None: raise ValueError('name cannot be None.')
        if args is None: raise ValueError('args cannot be None.')
        if body is None: body = []
        if decorator_list is None: decorator_list = []
        return ast.AsyncFunctionDef(name, args, body, decorator_list, returns)

class ClassDef(metaclass=SupertypeMeta):
    __past__ = ast.ClassDef
    def __new__(self, name=None, bases=None, keywords=None, body=None, decorator_list=None):
        """start checking validation"""
        if name is None: raise ValueError('name cannot be None.')
        if bases is None: bases = []
        if keywords is None: keywords = []
        if body is None: body = []
        if decorator_list is None: decorator_list = []
        return ast.ClassDef(name, bases, keywords, body, decorator_list)

class Return(metaclass=SupertypeMeta):
    __past__ = ast.Return
    def __new__(self, value=None):
        """start checking validation"""
        return ast.Return(value)

class Delete(metaclass=SupertypeMeta):
    __past__ = ast.Delete
    def __new__(self, targets=None):
        """start checking validation"""
        if targets is None: targets = []
        return ast.Delete(targets)

class Assign(metaclass=SupertypeMeta):
    __past__ = ast.Assign
    def __new__(self, targets=None, value=None):
        """start checking validation"""
        if targets is None: targets = []
        if value is None: raise ValueError('value cannot be None.')
        return ast.Assign(targets, value)

class AugAssign(metaclass=SupertypeMeta):
    __past__ = ast.AugAssign
    def __new__(self, target=None, op=None, value=None):
        """start checking validation"""
        if target is None: raise ValueError('target cannot be None.')
        if op is None: raise ValueError('op cannot be None.')
        if value is None: raise ValueError('value cannot be None.')
        return ast.AugAssign(target, op, value)

class AnnAssign(metaclass=SupertypeMeta):
    __past__ = ast.AnnAssign
    def __new__(self, target=None, annotation=None, value=None, simple=None):
        """start checking validation"""
        if target is None: raise ValueError('target cannot be None.')
        if annotation is None: raise ValueError('annotation cannot be None.')
        if simple is None: raise ValueError('simple cannot be None.')
        return ast.AnnAssign(target, annotation, value, simple)

class For(metaclass=SupertypeMeta):
    __past__ = ast.For
    def __new__(self, target=None, iter=None, body=None, orelse=None):
        """start checking validation"""
        if target is None: raise ValueError('target cannot be None.')
        if iter is None: raise ValueError('iter cannot be None.')
        if body is None: body = []
        if orelse is None: orelse = []
        return ast.For(target, iter, body, orelse)

class AsyncFor(metaclass=SupertypeMeta):
    __past__ = ast.AsyncFor
    def __new__(self, target=None, iter=None, body=None, orelse=None):
        """start checking validation"""
        if target is None: raise ValueError('target cannot be None.')
        if iter is None: raise ValueError('iter cannot be None.')
        if body is None: body = []
        if orelse is None: orelse = []
        return ast.AsyncFor(target, iter, body, orelse)

class While(metaclass=SupertypeMeta):
    __past__ = ast.While
    def __new__(self, test=None, body=None, orelse=None):
        """start checking validation"""
        if test is None: raise ValueError('test cannot be None.')
        if body is None: body = []
        if orelse is None: orelse = []
        return ast.While(test, body, orelse)

class If(metaclass=SupertypeMeta):
    __past__ = ast.If
    def __new__(self, test=None, body=None, orelse=None):
        """start checking validation"""
        if test is None: raise ValueError('test cannot be None.')
        if body is None: body = []
        if orelse is None: orelse = []
        return ast.If(test, body, orelse)

class With(metaclass=SupertypeMeta):
    __past__ = ast.With
    def __new__(self, items=None, body=None):
        """start checking validation"""
        if items is None: items = []
        if body is None: body = []
        return ast.With(items, body)

class AsyncWith(metaclass=SupertypeMeta):
    __past__ = ast.AsyncWith
    def __new__(self, items=None, body=None):
        """start checking validation"""
        if items is None: items = []
        if body is None: body = []
        return ast.AsyncWith(items, body)

class Raise(metaclass=SupertypeMeta):
    __past__ = ast.Raise
    def __new__(self, exc=None, cause=None):
        """start checking validation"""
        return ast.Raise(exc, cause)

class Try(metaclass=SupertypeMeta):
    __past__ = ast.Try
    def __new__(self, body=None, handlers=None, orelse=None, finalbody=None):
        """start checking validation"""
        if body is None: body = []
        if handlers is None: handlers = []
        if orelse is None: orelse = []
        if finalbody is None: finalbody = []
        return ast.Try(body, handlers, orelse, finalbody)

class Assert(metaclass=SupertypeMeta):
    __past__ = ast.Assert
    def __new__(self, test=None, msg=None):
        """start checking validation"""
        if test is None: raise ValueError('test cannot be None.')
        return ast.Assert(test, msg)

class Import(metaclass=SupertypeMeta):
    __past__ = ast.Import
    def __new__(self, names=None):
        """start checking validation"""
        if names is None: names = []
        return ast.Import(names)

class ImportFrom(metaclass=SupertypeMeta):
    __past__ = ast.ImportFrom
    def __new__(self, module=None, names=None, level=None):
        """start checking validation"""
        if names is None: names = []
        return ast.ImportFrom(module, names, level)

class Global(metaclass=SupertypeMeta):
    __past__ = ast.Global
    def __new__(self, names=None):
        """start checking validation"""
        if names is None: names = []
        return ast.Global(names)

class Nonlocal(metaclass=SupertypeMeta):
    __past__ = ast.Nonlocal
    def __new__(self, names=None):
        """start checking validation"""
        if names is None: names = []
        return ast.Nonlocal(names)

class Expr(metaclass=SupertypeMeta):
    __past__ = ast.Expr
    def __new__(self, value=None):
        """start checking validation"""
        if value is None: raise ValueError('value cannot be None.')
        return ast.Expr(value)

class Pass(metaclass=SupertypeMeta):
    __past__ = ast.Pass
    def __new__(self):
        """start checking validation"""
        return ast.Pass()

class Break(metaclass=SupertypeMeta):
    __past__ = ast.Break
    def __new__(self):
        """start checking validation"""
        return ast.Break()

class Continue(metaclass=SupertypeMeta):
    __past__ = ast.Continue
    def __new__(self):
        """start checking validation"""
        return ast.Continue()

class BoolOp(metaclass=SupertypeMeta):
    __past__ = ast.BoolOp
    def __new__(self, op=None, values=None):
        """start checking validation"""
        if op is None: raise ValueError('op cannot be None.')
        if values is None: values = []
        return ast.BoolOp(op, values)

class BinOp(metaclass=SupertypeMeta):
    __past__ = ast.BinOp
    def __new__(self, left=None, op=None, right=None):
        """start checking validation"""
        if left is None: raise ValueError('left cannot be None.')
        if op is None: raise ValueError('op cannot be None.')
        if right is None: raise ValueError('right cannot be None.')
        return ast.BinOp(left, op, right)

class UnaryOp(metaclass=SupertypeMeta):
    __past__ = ast.UnaryOp
    def __new__(self, op=None, operand=None):
        """start checking validation"""
        if op is None: raise ValueError('op cannot be None.')
        if operand is None: raise ValueError('operand cannot be None.')
        return ast.UnaryOp(op, operand)

class Lambda(metaclass=SupertypeMeta):
    __past__ = ast.Lambda
    def __new__(self, args=None, body=None):
        """start checking validation"""
        if args is None: raise ValueError('args cannot be None.')
        if body is None: raise ValueError('body cannot be None.')
        return ast.Lambda(args, body)

class IfExp(metaclass=SupertypeMeta):
    __past__ = ast.IfExp
    def __new__(self, test=None, body=None, orelse=None):
        """start checking validation"""
        if test is None: raise ValueError('test cannot be None.')
        if body is None: raise ValueError('body cannot be None.')
        if orelse is None: raise ValueError('orelse cannot be None.')
        return ast.IfExp(test, body, orelse)

class Dict(metaclass=SupertypeMeta):
    __past__ = ast.Dict
    def __new__(self, keys=None, values=None):
        """start checking validation"""
        if keys is None: keys = []
        if values is None: values = []
        return ast.Dict(keys, values)

class Set(metaclass=SupertypeMeta):
    __past__ = ast.Set
    def __new__(self, elts=None):
        """start checking validation"""
        if elts is None: elts = []
        return ast.Set(elts)

class ListComp(metaclass=SupertypeMeta):
    __past__ = ast.ListComp
    def __new__(self, elt=None, generators=None):
        """start checking validation"""
        if elt is None: raise ValueError('elt cannot be None.')
        if generators is None: generators = []
        return ast.ListComp(elt, generators)

class SetComp(metaclass=SupertypeMeta):
    __past__ = ast.SetComp
    def __new__(self, elt=None, generators=None):
        """start checking validation"""
        if elt is None: raise ValueError('elt cannot be None.')
        if generators is None: generators = []
        return ast.SetComp(elt, generators)

class DictComp(metaclass=SupertypeMeta):
    __past__ = ast.DictComp
    def __new__(self, key=None, value=None, generators=None):
        """start checking validation"""
        if key is None: raise ValueError('key cannot be None.')
        if value is None: raise ValueError('value cannot be None.')
        if generators is None: generators = []
        return ast.DictComp(key, value, generators)

class GeneratorExp(metaclass=SupertypeMeta):
    __past__ = ast.GeneratorExp
    def __new__(self, elt=None, generators=None):
        """start checking validation"""
        if elt is None: raise ValueError('elt cannot be None.')
        if generators is None: generators = []
        return ast.GeneratorExp(elt, generators)

class Await(metaclass=SupertypeMeta):
    __past__ = ast.Await
    def __new__(self, value=None):
        """start checking validation"""
        if value is None: raise ValueError('value cannot be None.')
        return ast.Await(value)

class Yield(metaclass=SupertypeMeta):
    __past__ = ast.Yield
    def __new__(self, value=None):
        """start checking validation"""
        return ast.Yield(value)

class YieldFrom(metaclass=SupertypeMeta):
    __past__ = ast.YieldFrom
    def __new__(self, value=None):
        """start checking validation"""
        if value is None: raise ValueError('value cannot be None.')
        return ast.YieldFrom(value)

class Compare(metaclass=SupertypeMeta):
    __past__ = ast.Compare
    def __new__(self, left=None, ops=None, comparators=None):
        """start checking validation"""
        if left is None: raise ValueError('left cannot be None.')
        if ops is None: ops = []
        if comparators is None: comparators = []
        return ast.Compare(left, ops, comparators)

class Call(metaclass=SupertypeMeta):
    __past__ = ast.Call
    def __new__(self, func=None, args=None, keywords=None):
        """start checking validation"""
        if func is None: raise ValueError('func cannot be None.')
        if args is None: args = []
        if keywords is None: keywords = []
        return ast.Call(func, args, keywords)

class Num(metaclass=SupertypeMeta):
    __past__ = ast.Num
    def __new__(self, n=None):
        """start checking validation"""
        if n is None: raise ValueError('n cannot be None.')
        return ast.Num(n)

class Str(metaclass=SupertypeMeta):
    __past__ = ast.Str
    def __new__(self, s=None):
        """start checking validation"""
        if s is None: raise ValueError('s cannot be None.')
        return ast.Str(s)

class FormattedValue(metaclass=SupertypeMeta):
    __past__ = ast.FormattedValue
    def __new__(self, value=None, conversion=None, format_spec=None):
        """start checking validation"""
        if value is None: raise ValueError('value cannot be None.')
        return ast.FormattedValue(value, conversion, format_spec)

class JoinedStr(metaclass=SupertypeMeta):
    __past__ = ast.JoinedStr
    def __new__(self, values=None):
        """start checking validation"""
        if values is None: values = []
        return ast.JoinedStr(values)

class Bytes(metaclass=SupertypeMeta):
    __past__ = ast.Bytes
    def __new__(self, s=None):
        """start checking validation"""
        if s is None: raise ValueError('s cannot be None.')
        return ast.Bytes(s)

class NameConstant(metaclass=SupertypeMeta):
    __past__ = ast.NameConstant
    def __new__(self, value=None):
        """start checking validation"""
        if value is None: raise ValueError('value cannot be None.')
        return ast.NameConstant(value)

class Ellipsis(metaclass=SupertypeMeta):
    __past__ = ast.Ellipsis
    def __new__(self):
        """start checking validation"""
        return ast.Ellipsis()

class Constant(metaclass=SupertypeMeta):
    __past__ = ast.Constant
    def __new__(self, value=None):
        """start checking validation"""
        if value is None: raise ValueError('value cannot be None.')
        return ast.Constant(value)

class Attribute(metaclass=SupertypeMeta):
    __past__ = ast.Attribute
    def __new__(self, value=None, attr=None, ctx=None):
        """start checking validation"""
        if value is None: raise ValueError('value cannot be None.')
        if attr is None: raise ValueError('attr cannot be None.')
        if ctx is None: raise ValueError('ctx cannot be None.')
        return ast.Attribute(value, attr, ctx)

class Subscript(metaclass=SupertypeMeta):
    __past__ = ast.Subscript
    def __new__(self, value=None, slice=None, ctx=None):
        """start checking validation"""
        if value is None: raise ValueError('value cannot be None.')
        if slice is None: raise ValueError('slice cannot be None.')
        if ctx is None: raise ValueError('ctx cannot be None.')
        return ast.Subscript(value, slice, ctx)

class Starred(metaclass=SupertypeMeta):
    __past__ = ast.Starred
    def __new__(self, value=None, ctx=None):
        """start checking validation"""
        if value is None: raise ValueError('value cannot be None.')
        if ctx is None: raise ValueError('ctx cannot be None.')
        return ast.Starred(value, ctx)

class Name(metaclass=SupertypeMeta):
    __past__ = ast.Name
    def __new__(self, id=None, ctx=None):
        """start checking validation"""
        if id is None: raise ValueError('id cannot be None.')
        if ctx is None: raise ValueError('ctx cannot be None.')
        return ast.Name(id, ctx)

class List(metaclass=SupertypeMeta):
    __past__ = ast.List
    def __new__(self, elts=None, ctx=None):
        """start checking validation"""
        if elts is None: elts = []
        if ctx is None: raise ValueError('ctx cannot be None.')
        return ast.List(elts, ctx)

class Tuple(metaclass=SupertypeMeta):
    __past__ = ast.Tuple
    def __new__(self, elts=None, ctx=None):
        """start checking validation"""
        if elts is None: elts = []
        if ctx is None: raise ValueError('ctx cannot be None.')
        return ast.Tuple(elts, ctx)

class Load(metaclass=SupertypeMeta):
    __past__ = ast.Load
    def __new__(self):
        """start checking validation"""
        return ast.Load()

class Store(metaclass=SupertypeMeta):
    __past__ = ast.Store
    def __new__(self):
        """start checking validation"""
        return ast.Store()

class Del(metaclass=SupertypeMeta):
    __past__ = ast.Del
    def __new__(self):
        """start checking validation"""
        return ast.Del()

class AugLoad(metaclass=SupertypeMeta):
    __past__ = ast.AugLoad
    def __new__(self):
        """start checking validation"""
        return ast.AugLoad()

class AugStore(metaclass=SupertypeMeta):
    __past__ = ast.AugStore
    def __new__(self):
        """start checking validation"""
        return ast.AugStore()

class Param(metaclass=SupertypeMeta):
    __past__ = ast.Param
    def __new__(self):
        """start checking validation"""
        return ast.Param()

class Slice(metaclass=SupertypeMeta):
    __past__ = ast.Slice
    def __new__(self, lower=None, upper=None, step=None):
        """start checking validation"""
        return ast.Slice(lower, upper, step)

class ExtSlice(metaclass=SupertypeMeta):
    __past__ = ast.ExtSlice
    def __new__(self, dims=None):
        """start checking validation"""
        if dims is None: dims = []
        return ast.ExtSlice(dims)

class Index(metaclass=SupertypeMeta):
    __past__ = ast.Index
    def __new__(self, value=None):
        """start checking validation"""
        if value is None: raise ValueError('value cannot be None.')
        return ast.Index(value)

class And(metaclass=SupertypeMeta):
    __past__ = ast.And
    def __new__(self):
        """start checking validation"""
        return ast.And()

class Or(metaclass=SupertypeMeta):
    __past__ = ast.Or
    def __new__(self):
        """start checking validation"""
        return ast.Or()

class Add(metaclass=SupertypeMeta):
    __past__ = ast.Add
    def __new__(self):
        """start checking validation"""
        return ast.Add()

class Sub(metaclass=SupertypeMeta):
    __past__ = ast.Sub
    def __new__(self):
        """start checking validation"""
        return ast.Sub()

class Mult(metaclass=SupertypeMeta):
    __past__ = ast.Mult
    def __new__(self):
        """start checking validation"""
        return ast.Mult()

class MatMult(metaclass=SupertypeMeta):
    __past__ = ast.MatMult
    def __new__(self):
        """start checking validation"""
        return ast.MatMult()

class Div(metaclass=SupertypeMeta):
    __past__ = ast.Div
    def __new__(self):
        """start checking validation"""
        return ast.Div()

class Mod(metaclass=SupertypeMeta):
    __past__ = ast.Mod
    def __new__(self):
        """start checking validation"""
        return ast.Mod()

class Pow(metaclass=SupertypeMeta):
    __past__ = ast.Pow
    def __new__(self):
        """start checking validation"""
        return ast.Pow()

class LShift(metaclass=SupertypeMeta):
    __past__ = ast.LShift
    def __new__(self):
        """start checking validation"""
        return ast.LShift()

class RShift(metaclass=SupertypeMeta):
    __past__ = ast.RShift
    def __new__(self):
        """start checking validation"""
        return ast.RShift()

class BitOr(metaclass=SupertypeMeta):
    __past__ = ast.BitOr
    def __new__(self):
        """start checking validation"""
        return ast.BitOr()

class BitXor(metaclass=SupertypeMeta):
    __past__ = ast.BitXor
    def __new__(self):
        """start checking validation"""
        return ast.BitXor()

class BitAnd(metaclass=SupertypeMeta):
    __past__ = ast.BitAnd
    def __new__(self):
        """start checking validation"""
        return ast.BitAnd()

class FloorDiv(metaclass=SupertypeMeta):
    __past__ = ast.FloorDiv
    def __new__(self):
        """start checking validation"""
        return ast.FloorDiv()

class Invert(metaclass=SupertypeMeta):
    __past__ = ast.Invert
    def __new__(self):
        """start checking validation"""
        return ast.Invert()

class Not(metaclass=SupertypeMeta):
    __past__ = ast.Not
    def __new__(self):
        """start checking validation"""
        return ast.Not()

class UAdd(metaclass=SupertypeMeta):
    __past__ = ast.UAdd
    def __new__(self):
        """start checking validation"""
        return ast.UAdd()

class USub(metaclass=SupertypeMeta):
    __past__ = ast.USub
    def __new__(self):
        """start checking validation"""
        return ast.USub()

class Eq(metaclass=SupertypeMeta):
    __past__ = ast.Eq
    def __new__(self):
        """start checking validation"""
        return ast.Eq()

class NotEq(metaclass=SupertypeMeta):
    __past__ = ast.NotEq
    def __new__(self):
        """start checking validation"""
        return ast.NotEq()

class Lt(metaclass=SupertypeMeta):
    __past__ = ast.Lt
    def __new__(self):
        """start checking validation"""
        return ast.Lt()

class LtE(metaclass=SupertypeMeta):
    __past__ = ast.LtE
    def __new__(self):
        """start checking validation"""
        return ast.LtE()

class Gt(metaclass=SupertypeMeta):
    __past__ = ast.Gt
    def __new__(self):
        """start checking validation"""
        return ast.Gt()

class GtE(metaclass=SupertypeMeta):
    __past__ = ast.GtE
    def __new__(self):
        """start checking validation"""
        return ast.GtE()

class Is(metaclass=SupertypeMeta):
    __past__ = ast.Is
    def __new__(self):
        """start checking validation"""
        return ast.Is()

class IsNot(metaclass=SupertypeMeta):
    __past__ = ast.IsNot
    def __new__(self):
        """start checking validation"""
        return ast.IsNot()

class In(metaclass=SupertypeMeta):
    __past__ = ast.In
    def __new__(self):
        """start checking validation"""
        return ast.In()

class NotIn(metaclass=SupertypeMeta):
    __past__ = ast.NotIn
    def __new__(self):
        """start checking validation"""
        return ast.NotIn()

class comprehension(metaclass=SupertypeMeta):
    __past__ = ast.comprehension
    def __new__(self, target=None, iter=None, ifs=None, is_async=None):
        """start checking validation"""
        if target is None: raise ValueError('target cannot be None.')
        if iter is None: raise ValueError('iter cannot be None.')
        if ifs is None: ifs = []
        if is_async is None: raise ValueError('is_async cannot be None.')
        return ast.comprehension(target, iter, ifs, is_async)

class ExceptHandler(metaclass=SupertypeMeta):
    __past__ = ast.ExceptHandler
    def __new__(self, type=None, name=None, body=None):
        """start checking validation"""
        if body is None: body = []
        return ast.ExceptHandler(type, name, body)

class arguments(metaclass=SupertypeMeta):
    __past__ = ast.arguments
    def __new__(self, args=None, vararg=None, kwonlyargs=None, kw_defaults=None, kwarg=None, defaults=None):
        """start checking validation"""
        if args is None: args = []
        if kwonlyargs is None: kwonlyargs = []
        if kw_defaults is None: kw_defaults = []
        if defaults is None: defaults = []
        return ast.arguments(args, vararg, kwonlyargs, kw_defaults, kwarg, defaults)

class arg(metaclass=SupertypeMeta):
    __past__ = ast.arg
    def __new__(self, arg=None, annotation=None):
        """start checking validation"""
        if arg is None: raise ValueError('arg cannot be None.')
        return ast.arg(arg, annotation)

class keyword(metaclass=SupertypeMeta):
    __past__ = ast.keyword
    def __new__(self, arg=None, value=None):
        """start checking validation"""
        if value is None: raise ValueError('value cannot be None.')
        return ast.keyword(arg, value)

class alias(metaclass=SupertypeMeta):
    __past__ = ast.alias
    def __new__(self, name=None, asname=None):
        """start checking validation"""
        if name is None: raise ValueError('name cannot be None.')
        return ast.alias(name, asname)

class withitem(metaclass=SupertypeMeta):
    __past__ = ast.withitem
    def __new__(self, context_expr=None, optional_vars=None):
        """start checking validation"""
        if context_expr is None: raise ValueError('context_expr cannot be None.')
        return ast.withitem(context_expr, optional_vars)

