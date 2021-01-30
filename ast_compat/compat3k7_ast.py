import ast
from .make import *
_unset = object()

class Module(metaclass=SupertypeMeta):
    __past__ = ast.Module
    def __new__(self, body=_unset):
        """start checking validation"""
        if body is _unset: body = []
        return ast.Module(body)

class Interactive(metaclass=SupertypeMeta):
    __past__ = ast.Interactive
    def __new__(self, body=_unset):
        """start checking validation"""
        if body is _unset: body = []
        return ast.Interactive(body)

class Expression(metaclass=SupertypeMeta):
    __past__ = ast.Expression
    def __new__(self, body=_unset):
        """start checking validation"""
        if body is _unset: raise ValueError('body cannot be None.')
        return ast.Expression(body)

class Suite(metaclass=SupertypeMeta):
    __past__ = ast.Suite
    def __new__(self, body=_unset):
        """start checking validation"""
        if body is _unset: body = []
        return ast.Suite(body)

class FunctionDef(metaclass=SupertypeMeta):
    __past__ = ast.FunctionDef
    def __new__(self, name=_unset, args=_unset, body=_unset, decorator_list=_unset, returns=_unset):
        """start checking validation"""
        if name is _unset: raise ValueError('name cannot be None.')
        if args is _unset: raise ValueError('args cannot be None.')
        if body is _unset: body = []
        if decorator_list is _unset: decorator_list = []
        if returns is _unset: returns = None
        return ast.FunctionDef(name, args, body, decorator_list, returns)

class AsyncFunctionDef(metaclass=SupertypeMeta):
    __past__ = ast.AsyncFunctionDef
    def __new__(self, name=_unset, args=_unset, body=_unset, decorator_list=_unset, returns=_unset):
        """start checking validation"""
        if name is _unset: raise ValueError('name cannot be None.')
        if args is _unset: raise ValueError('args cannot be None.')
        if body is _unset: body = []
        if decorator_list is _unset: decorator_list = []
        if returns is _unset: returns = None
        return ast.AsyncFunctionDef(name, args, body, decorator_list, returns)

class ClassDef(metaclass=SupertypeMeta):
    __past__ = ast.ClassDef
    def __new__(self, name=_unset, bases=_unset, keywords=_unset, body=_unset, decorator_list=_unset):
        """start checking validation"""
        if name is _unset: raise ValueError('name cannot be None.')
        if bases is _unset: bases = []
        if keywords is _unset: keywords = []
        if body is _unset: body = []
        if decorator_list is _unset: decorator_list = []
        return ast.ClassDef(name, bases, keywords, body, decorator_list)

class Return(metaclass=SupertypeMeta):
    __past__ = ast.Return
    def __new__(self, value=_unset):
        """start checking validation"""
        if value is _unset: value = None
        return ast.Return(value)

class Delete(metaclass=SupertypeMeta):
    __past__ = ast.Delete
    def __new__(self, targets=_unset):
        """start checking validation"""
        if targets is _unset: targets = []
        return ast.Delete(targets)

class Assign(metaclass=SupertypeMeta):
    __past__ = ast.Assign
    def __new__(self, targets=_unset, value=_unset):
        """start checking validation"""
        if targets is _unset: targets = []
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.Assign(targets, value)

class AugAssign(metaclass=SupertypeMeta):
    __past__ = ast.AugAssign
    def __new__(self, target=_unset, op=_unset, value=_unset):
        """start checking validation"""
        if target is _unset: raise ValueError('target cannot be None.')
        if op is _unset: raise ValueError('op cannot be None.')
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.AugAssign(target, op, value)

class AnnAssign(metaclass=SupertypeMeta):
    __past__ = ast.AnnAssign
    def __new__(self, target=_unset, annotation=_unset, value=_unset, simple=_unset):
        """start checking validation"""
        if target is _unset: raise ValueError('target cannot be None.')
        if annotation is _unset: raise ValueError('annotation cannot be None.')
        if value is _unset: value = None
        if simple is _unset: raise ValueError('simple cannot be None.')
        return ast.AnnAssign(target, annotation, value, simple)

class For(metaclass=SupertypeMeta):
    __past__ = ast.For
    def __new__(self, target=_unset, iter=_unset, body=_unset, orelse=_unset):
        """start checking validation"""
        if target is _unset: raise ValueError('target cannot be None.')
        if iter is _unset: raise ValueError('iter cannot be None.')
        if body is _unset: body = []
        if orelse is _unset: orelse = []
        return ast.For(target, iter, body, orelse)

class AsyncFor(metaclass=SupertypeMeta):
    __past__ = ast.AsyncFor
    def __new__(self, target=_unset, iter=_unset, body=_unset, orelse=_unset):
        """start checking validation"""
        if target is _unset: raise ValueError('target cannot be None.')
        if iter is _unset: raise ValueError('iter cannot be None.')
        if body is _unset: body = []
        if orelse is _unset: orelse = []
        return ast.AsyncFor(target, iter, body, orelse)

class While(metaclass=SupertypeMeta):
    __past__ = ast.While
    def __new__(self, test=_unset, body=_unset, orelse=_unset):
        """start checking validation"""
        if test is _unset: raise ValueError('test cannot be None.')
        if body is _unset: body = []
        if orelse is _unset: orelse = []
        return ast.While(test, body, orelse)

class If(metaclass=SupertypeMeta):
    __past__ = ast.If
    def __new__(self, test=_unset, body=_unset, orelse=_unset):
        """start checking validation"""
        if test is _unset: raise ValueError('test cannot be None.')
        if body is _unset: body = []
        if orelse is _unset: orelse = []
        return ast.If(test, body, orelse)

class With(metaclass=SupertypeMeta):
    __past__ = ast.With
    def __new__(self, items=_unset, body=_unset):
        """start checking validation"""
        if items is _unset: items = []
        if body is _unset: body = []
        return ast.With(items, body)

class AsyncWith(metaclass=SupertypeMeta):
    __past__ = ast.AsyncWith
    def __new__(self, items=_unset, body=_unset):
        """start checking validation"""
        if items is _unset: items = []
        if body is _unset: body = []
        return ast.AsyncWith(items, body)

class Raise(metaclass=SupertypeMeta):
    __past__ = ast.Raise
    def __new__(self, exc=_unset, cause=_unset):
        """start checking validation"""
        if exc is _unset: exc = None
        if cause is _unset: cause = None
        return ast.Raise(exc, cause)

class Try(metaclass=SupertypeMeta):
    __past__ = ast.Try
    def __new__(self, body=_unset, handlers=_unset, orelse=_unset, finalbody=_unset):
        """start checking validation"""
        if body is _unset: body = []
        if handlers is _unset: handlers = []
        if orelse is _unset: orelse = []
        if finalbody is _unset: finalbody = []
        return ast.Try(body, handlers, orelse, finalbody)

class Assert(metaclass=SupertypeMeta):
    __past__ = ast.Assert
    def __new__(self, test=_unset, msg=_unset):
        """start checking validation"""
        if test is _unset: raise ValueError('test cannot be None.')
        if msg is _unset: msg = None
        return ast.Assert(test, msg)

class Import(metaclass=SupertypeMeta):
    __past__ = ast.Import
    def __new__(self, names=_unset):
        """start checking validation"""
        if names is _unset: names = []
        return ast.Import(names)

class ImportFrom(metaclass=SupertypeMeta):
    __past__ = ast.ImportFrom
    def __new__(self, module=_unset, names=_unset, level=_unset):
        """start checking validation"""
        if module is _unset: module = None
        if names is _unset: names = []
        if level is _unset: level = None
        return ast.ImportFrom(module, names, level)

class Global(metaclass=SupertypeMeta):
    __past__ = ast.Global
    def __new__(self, names=_unset):
        """start checking validation"""
        if names is _unset: names = []
        return ast.Global(names)

class Nonlocal(metaclass=SupertypeMeta):
    __past__ = ast.Nonlocal
    def __new__(self, names=_unset):
        """start checking validation"""
        if names is _unset: names = []
        return ast.Nonlocal(names)

class Expr(metaclass=SupertypeMeta):
    __past__ = ast.Expr
    def __new__(self, value=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
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
    def __new__(self, op=_unset, values=_unset):
        """start checking validation"""
        if op is _unset: raise ValueError('op cannot be None.')
        if values is _unset: values = []
        return ast.BoolOp(op, values)

class BinOp(metaclass=SupertypeMeta):
    __past__ = ast.BinOp
    def __new__(self, left=_unset, op=_unset, right=_unset):
        """start checking validation"""
        if left is _unset: raise ValueError('left cannot be None.')
        if op is _unset: raise ValueError('op cannot be None.')
        if right is _unset: raise ValueError('right cannot be None.')
        return ast.BinOp(left, op, right)

class UnaryOp(metaclass=SupertypeMeta):
    __past__ = ast.UnaryOp
    def __new__(self, op=_unset, operand=_unset):
        """start checking validation"""
        if op is _unset: raise ValueError('op cannot be None.')
        if operand is _unset: raise ValueError('operand cannot be None.')
        return ast.UnaryOp(op, operand)

class Lambda(metaclass=SupertypeMeta):
    __past__ = ast.Lambda
    def __new__(self, args=_unset, body=_unset):
        """start checking validation"""
        if args is _unset: raise ValueError('args cannot be None.')
        if body is _unset: raise ValueError('body cannot be None.')
        return ast.Lambda(args, body)

class IfExp(metaclass=SupertypeMeta):
    __past__ = ast.IfExp
    def __new__(self, test=_unset, body=_unset, orelse=_unset):
        """start checking validation"""
        if test is _unset: raise ValueError('test cannot be None.')
        if body is _unset: raise ValueError('body cannot be None.')
        if orelse is _unset: raise ValueError('orelse cannot be None.')
        return ast.IfExp(test, body, orelse)

class Dict(metaclass=SupertypeMeta):
    __past__ = ast.Dict
    def __new__(self, keys=_unset, values=_unset):
        """start checking validation"""
        if keys is _unset: keys = []
        if values is _unset: values = []
        return ast.Dict(keys, values)

class Set(metaclass=SupertypeMeta):
    __past__ = ast.Set
    def __new__(self, elts=_unset):
        """start checking validation"""
        if elts is _unset: elts = []
        return ast.Set(elts)

class ListComp(metaclass=SupertypeMeta):
    __past__ = ast.ListComp
    def __new__(self, elt=_unset, generators=_unset):
        """start checking validation"""
        if elt is _unset: raise ValueError('elt cannot be None.')
        if generators is _unset: generators = []
        return ast.ListComp(elt, generators)

class SetComp(metaclass=SupertypeMeta):
    __past__ = ast.SetComp
    def __new__(self, elt=_unset, generators=_unset):
        """start checking validation"""
        if elt is _unset: raise ValueError('elt cannot be None.')
        if generators is _unset: generators = []
        return ast.SetComp(elt, generators)

class DictComp(metaclass=SupertypeMeta):
    __past__ = ast.DictComp
    def __new__(self, key=_unset, value=_unset, generators=_unset):
        """start checking validation"""
        if key is _unset: raise ValueError('key cannot be None.')
        if value is _unset: raise ValueError('value cannot be None.')
        if generators is _unset: generators = []
        return ast.DictComp(key, value, generators)

class GeneratorExp(metaclass=SupertypeMeta):
    __past__ = ast.GeneratorExp
    def __new__(self, elt=_unset, generators=_unset):
        """start checking validation"""
        if elt is _unset: raise ValueError('elt cannot be None.')
        if generators is _unset: generators = []
        return ast.GeneratorExp(elt, generators)

class Await(metaclass=SupertypeMeta):
    __past__ = ast.Await
    def __new__(self, value=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.Await(value)

class Yield(metaclass=SupertypeMeta):
    __past__ = ast.Yield
    def __new__(self, value=_unset):
        """start checking validation"""
        if value is _unset: value = None
        return ast.Yield(value)

class YieldFrom(metaclass=SupertypeMeta):
    __past__ = ast.YieldFrom
    def __new__(self, value=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.YieldFrom(value)

class Compare(metaclass=SupertypeMeta):
    __past__ = ast.Compare
    def __new__(self, left=_unset, ops=_unset, comparators=_unset):
        """start checking validation"""
        if left is _unset: raise ValueError('left cannot be None.')
        if ops is _unset: ops = []
        if comparators is _unset: comparators = []
        return ast.Compare(left, ops, comparators)

class Call(metaclass=SupertypeMeta):
    __past__ = ast.Call
    def __new__(self, func=_unset, args=_unset, keywords=_unset):
        """start checking validation"""
        if func is _unset: raise ValueError('func cannot be None.')
        if args is _unset: args = []
        if keywords is _unset: keywords = []
        return ast.Call(func, args, keywords)

class Num(metaclass=SupertypeMeta):
    __past__ = ast.Num
    def __new__(self, n=_unset):
        """start checking validation"""
        if n is _unset: raise ValueError('n cannot be None.')
        return ast.Num(n)

class Str(metaclass=SupertypeMeta):
    __past__ = ast.Str
    def __new__(self, s=_unset):
        """start checking validation"""
        if s is _unset: raise ValueError('s cannot be None.')
        return ast.Str(s)

class FormattedValue(metaclass=SupertypeMeta):
    __past__ = ast.FormattedValue
    def __new__(self, value=_unset, conversion=_unset, format_spec=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        if conversion is _unset: conversion = None
        if format_spec is _unset: format_spec = None
        return ast.FormattedValue(value, conversion, format_spec)

class JoinedStr(metaclass=SupertypeMeta):
    __past__ = ast.JoinedStr
    def __new__(self, values=_unset):
        """start checking validation"""
        if values is _unset: values = []
        return ast.JoinedStr(values)

class Bytes(metaclass=SupertypeMeta):
    __past__ = ast.Bytes
    def __new__(self, s=_unset):
        """start checking validation"""
        if s is _unset: raise ValueError('s cannot be None.')
        return ast.Bytes(s)

class NameConstant(metaclass=SupertypeMeta):
    __past__ = ast.NameConstant
    def __new__(self, value=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.NameConstant(value)

class Ellipsis(metaclass=SupertypeMeta):
    __past__ = ast.Ellipsis
    def __new__(self):
        """start checking validation"""
        return ast.Ellipsis()

class Constant(metaclass=SupertypeMeta):
    __past__ = ast.Constant
    def __new__(self, value=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.Constant(value)

class Attribute(metaclass=SupertypeMeta):
    __past__ = ast.Attribute
    def __new__(self, value=_unset, attr=_unset, ctx=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        if attr is _unset: raise ValueError('attr cannot be None.')
        if ctx is _unset: raise ValueError('ctx cannot be None.')
        return ast.Attribute(value, attr, ctx)

class Subscript(metaclass=SupertypeMeta):
    __past__ = ast.Subscript
    def __new__(self, value=_unset, slice=_unset, ctx=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        if slice is _unset: raise ValueError('slice cannot be None.')
        if ctx is _unset: raise ValueError('ctx cannot be None.')
        return ast.Subscript(value, slice, ctx)

class Starred(metaclass=SupertypeMeta):
    __past__ = ast.Starred
    def __new__(self, value=_unset, ctx=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
        if ctx is _unset: raise ValueError('ctx cannot be None.')
        return ast.Starred(value, ctx)

class Name(metaclass=SupertypeMeta):
    __past__ = ast.Name
    def __new__(self, id=_unset, ctx=_unset):
        """start checking validation"""
        if id is _unset: raise ValueError('id cannot be None.')
        if ctx is _unset: raise ValueError('ctx cannot be None.')
        return ast.Name(id, ctx)

class List(metaclass=SupertypeMeta):
    __past__ = ast.List
    def __new__(self, elts=_unset, ctx=_unset):
        """start checking validation"""
        if elts is _unset: elts = []
        if ctx is _unset: raise ValueError('ctx cannot be None.')
        return ast.List(elts, ctx)

class Tuple(metaclass=SupertypeMeta):
    __past__ = ast.Tuple
    def __new__(self, elts=_unset, ctx=_unset):
        """start checking validation"""
        if elts is _unset: elts = []
        if ctx is _unset: raise ValueError('ctx cannot be None.')
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
    def __new__(self, lower=_unset, upper=_unset, step=_unset):
        """start checking validation"""
        if lower is _unset: lower = None
        if upper is _unset: upper = None
        if step is _unset: step = None
        return ast.Slice(lower, upper, step)

class ExtSlice(metaclass=SupertypeMeta):
    __past__ = ast.ExtSlice
    def __new__(self, dims=_unset):
        """start checking validation"""
        if dims is _unset: dims = []
        return ast.ExtSlice(dims)

class Index(metaclass=SupertypeMeta):
    __past__ = ast.Index
    def __new__(self, value=_unset):
        """start checking validation"""
        if value is _unset: raise ValueError('value cannot be None.')
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
    def __new__(self, target=_unset, iter=_unset, ifs=_unset, is_async=_unset):
        """start checking validation"""
        if target is _unset: raise ValueError('target cannot be None.')
        if iter is _unset: raise ValueError('iter cannot be None.')
        if ifs is _unset: ifs = []
        if is_async is _unset: raise ValueError('is_async cannot be None.')
        return ast.comprehension(target, iter, ifs, is_async)

class ExceptHandler(metaclass=SupertypeMeta):
    __past__ = ast.ExceptHandler
    def __new__(self, type=_unset, name=_unset, body=_unset):
        """start checking validation"""
        if type is _unset: type = None
        if name is _unset: name = None
        if body is _unset: body = []
        return ast.ExceptHandler(type, name, body)

class arguments(metaclass=SupertypeMeta):
    __past__ = ast.arguments
    def __new__(self, args=_unset, vararg=_unset, kwonlyargs=_unset, kw_defaults=_unset, kwarg=_unset, defaults=_unset):
        """start checking validation"""
        if args is _unset: args = []
        if vararg is _unset: vararg = None
        if kwonlyargs is _unset: kwonlyargs = []
        if kw_defaults is _unset: kw_defaults = []
        if kwarg is _unset: kwarg = None
        if defaults is _unset: defaults = []
        return ast.arguments(args, vararg, kwonlyargs, kw_defaults, kwarg, defaults)

class arg(metaclass=SupertypeMeta):
    __past__ = ast.arg
    def __new__(self, arg=_unset, annotation=_unset):
        """start checking validation"""
        if arg is _unset: raise ValueError('arg cannot be None.')
        if annotation is _unset: annotation = None
        return ast.arg(arg, annotation)

class keyword(metaclass=SupertypeMeta):
    __past__ = ast.keyword
    def __new__(self, arg=_unset, value=_unset):
        """start checking validation"""
        if arg is _unset: arg = None
        if value is _unset: raise ValueError('value cannot be None.')
        return ast.keyword(arg, value)

class alias(metaclass=SupertypeMeta):
    __past__ = ast.alias
    def __new__(self, name=_unset, asname=_unset):
        """start checking validation"""
        if name is _unset: raise ValueError('name cannot be None.')
        if asname is _unset: asname = None
        return ast.alias(name, asname)

class withitem(metaclass=SupertypeMeta):
    __past__ = ast.withitem
    def __new__(self, context_expr=_unset, optional_vars=_unset):
        """start checking validation"""
        if context_expr is _unset: raise ValueError('context_expr cannot be None.')
        if optional_vars is _unset: optional_vars = None
        return ast.withitem(context_expr, optional_vars)

