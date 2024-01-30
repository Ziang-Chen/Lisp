import uuid

"""
Token For ASt

API:
Tokens.Auto
Tokens.Add
Tokens.And
Tokens.AnnAssign
Tokens.Assert
Tokens.Assign
Tokens.AsyncFor
Tokens.AsyncFunctionDef
Tokens.AsyncWith
Tokens.AsyncWithItem
Tokens.Attribute
Tokens.AugAssign
Tokens.BitwiseAnd
Tokens.BitwiseNot
Tokens.BitwiseOr
Tokens.BitwiseXor
Tokens.Boolean
Tokens.Break
Tokens.Call
Tokens.ClassDef
Tokens.Continue
Tokens.Delete
Tokens.Dict
Tokens.Divide
Tokens.Ellipsis
Tokens.Equal
Tokens.ExceptHandler
Tokens.Exec
Tokens.FloorDivide
Tokens.For
Tokens.FunctionDef
Tokens.Global
Tokens.GreaterThan
Tokens.GreaterThanEqual
Tokens.If
Tokens.Import
Tokens.ImportFrom
Tokens.In
Tokens.Index
Tokens.Is
Tokens.IsNot
Tokens.Lambda
Tokens.LeftShift
Tokens.LessThan
Tokens.LessThanEqual
Tokens.List
Tokens.Map
Tokens.Modulo
Tokens.Multiply
Tokens.Name
Tokens.NameConstant
Tokens.New
Tokens.NoneType
Tokens.Nonlocal
Tokens.Not
Tokens.NotEqual
Tokens.NotIn
Tokens.Number
Tokens.Or
Tokens.Pass
Tokens.Power
Tokens.Print
Tokens.Raise
Tokens.Return
Tokens.RightShift
Tokens.Set
Tokens.Slice
Tokens.String
Tokens.Struct
Tokens.Subtract
Tokens.Try
Tokens.Tuple
Tokens.TypeDef
Tokens.UnaryAdd
Tokens.UnaryInvert
Tokens.UnarySubtract
Tokens.Variable
Tokens.While
Tokens.With
Tokens.WithItem
Tokens.Yield
Tokens.YieldFrom


"""


class Map:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Map({self.value})"

    def __str__(self):
        return self.__repr__()


class Else:
    def __init__(self, body=None):
        self.body = body
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Else({self.body})"

    def __str__(self):
        return self.__repr__()


class Block:
    def __init__(self, body=None):
        self.body = body
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Block({self.body})"


class Struct:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Struct({self.value})"


class Auto:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Auto({self.value})"


class New:
    def __init__(self, name=None, args=None):
        self.name = name
        self.args = args
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"New({self.name}, {self.args})"


class TypeDef:
    def __init__(self, name=None, bases=None, keywords=None, body=None):
        self.name = name
        self.bases = bases
        self.keywords = keywords
        self.body = body
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"TypeDef({self.name}, {self.bases}, {self.keywords}, {self.body})"


class Print:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Print({self.value})"


class Add:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Add({self.left}, {self.right})"


class Variable:
    def __init__(self, name=None):
        self.name = name
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Variable({self.name})"


class Number:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Number({self.value})"


class Multiply:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Multiply({self.left}, {self.right})"


class Divide:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Divide({self.left}, {self.right})"


class Subtract:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Subtract({self.left}, {self.right})"


class Power:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Power({self.left}, {self.right})"


class Modulo:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Modulo({self.left}, {self.right})"


class FloorDivide:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"FloorDivide({self.left}, {self.right})"


class BitwiseAnd:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"BitwiseAnd({self.left}, {self.right})"


class BitwiseOr:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"BitwiseOr({self.left}, {self.right})"


class BitwiseXor:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"BitwiseXor({self.left}, {self.right})"


class BitwiseNot:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"BitwiseNot({self.value})"


class LeftShift:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"LeftShift({self.left}, {self.right})"


class RightShift:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"RightShift({self.left}, {self.right})"


class LessThan:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"LessThan({self.left}, {self.right})"


class LessThanEqual:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"LessThanEqual({self.left}, {self.right})"


class GreaterThan:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"GreaterThan({self.left}, {self.right})"


class GreaterThanEqual:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"GreaterThanEqual({self.left}, {self.right})"


class Equal:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Equal({self.left}, {self.right})"


class NotEqual:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"NotEqual({self.left}, {self.right})"


class And:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"And({self.left}, {self.right})"


class Or:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Or({self.left}, {self.right})"


class Not:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Not({self.value})"


class In:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"In({self.left}, {self.right})"


class NotIn:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"NotIn({self.left}, {self.right})"


class Is:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Is({self.left}, {self.right})"


class IsNot:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"IsNot({self.left}, {self.right})"


class UnaryAdd:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"UnaryAdd({self.value})"


class UnarySubtract:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"UnarySubtract({self.value})"


class UnaryInvert:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"UnaryInvert({self.value})"


class Call:
    def __init__(self, func=None, args=None):
        self.func = func
        self.args = args
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Call({self.func}, {self.args})"


class Index:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Index({self.value})"


class Slice:
    def __init__(self, start=None, stop=None, step=None):
        self.start = start
        self.stop = stop
        self.step = step
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Slice({self.start}, {self.stop}, {self.step})"


class Tuple:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Tuple({self.value})"


class List:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"List({self.value})"


class Set:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Set({self.value})"


class Dict:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Dict({self.value})"


class String:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"String({self.value})"


class Boolean:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Boolean({self.value})"


class NoneType:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"NoneType({self.value})"


class Ellipsis:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Ellipsis({self.value})"


class NameConstant:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"NameConstant({self.value})"


class Name:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Name({self.value})"


class Attribute:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Attribute({self.value})"


class Lambda:
    def __init__(self, args, body):
        self.args = args
        self.body = body
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Lambda({self.args}, {self.body})"


class If:
    def __init__(self, condition=None, body=None, else_body=None):
        self.condition = condition
        self.body = body
        self.else_body = else_body
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"If({self.condition}, {self.body}, {self.else_body})"


class For:
    def __init__(self, target=None, iter=None, body=None, else_body=None):
        self.target = target
        self.iter = iter
        self.body = body
        self.else_body = else_body
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"For({self.target}, {self.iter}, {self.body}, {self.else_body})"


class While:
    def __init__(self, condition=None, body=None, else_body=None):
        self.condition = condition
        self.body = body
        self.else_body = else_body
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"While({self.condition}, {self.body}, {self.else_body})"


class Break:
    def __init__(self):
        self.id = uuid.uuid4()
        pass

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Break()"


class Continue:
    def __init__(self):
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Continue()"


class Pass:
    def __init__(self):
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Pass()"


class Return:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Return({self.value})"


class Yield:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Yield({self.value})"


class YieldFrom:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"YieldFrom({self.value})"


class Assert:
    def __init__(self, condition=None, message=None):
        self.condition = condition
        self.message = message
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Assert({self.condition}, {self.message})"


class Import:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return "Import({self.value})"


class ImportFrom:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return "ImportFrom({self.value})"


class Global:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return "Global({self.value})"


class Nonlocal:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return "Nonlocal({self.value})"


class Exec:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return "Exec({self.value})"


class Delete:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return "Delete({self.value})"


class Try:
    def __init__(self, body=None, handlers=None, else_body=None, finally_body=None):
        self.body = body
        self.handlers = handlers
        self.else_body = else_body
        self.finally_body = finally_body
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return (
            f"Try({self.body}, {self.handlers}, {self.else_body}, {self.finally_body})"
        )


class ExceptHandler:
    def __init__(self, exception=None, target=None, body=None):
        self.exception = exception
        self.target = target
        self.body = body
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"ExceptHandler({self.exception}, {self.target}, {self.body})"


class Raise:
    def __init__(self, exception=None, cause=None):
        self.exception = exception
        self.cause = cause
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Raise({self.exception}, {self.cause})"


class With:
    def __init__(self, items=None, body=None):
        self.items = items
        self.body = body
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"With({self.items}, {self.body})"


class WithItem:
    def __init__(self, target=None, value=None):
        self.target = target
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"WithItem({self.target}, {self.value})"


class FunctionDef:
    def __init__(self, name=None, args=None, body=None, decorator_list=None):
        self.name = name
        self.args = args
        self.body = body
        self.decorator_list = decorator_list
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return (
            f"FunctionDef({self.name}, {self.args}, {self.body}, {self.decorator_list})"
        )


class ClassDef:
    def __init__(
        self, name=None, bases=None, keywords=None, body=None, decorator_list=None
    ):
        self.name = name
        self.bases = bases
        self.keywords = keywords
        self.body = body
        self.decorator_list = decorator_list
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"ClassDef({self.name}, {self.bases}, {self.keywords}, {self.body}, {self.decorator_list})"


class AsyncFunctionDef:
    def __init__(self, name=None, args=None, body=None, decorator_list=None):
        self.name = name
        self.args = args
        self.body = body
        self.decorator_list = decorator_list
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"AsyncFunctionDef({self.name}, {self.args}, {self.body}, {self.decorator_list})"


class AsyncWith:
    def __init__(self, items=None, body=None):
        self.items = items
        self.body = body
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"AsyncWith({self.items}, {self.body})"


class AsyncFor:
    def __init__(self, target=None, iter=None, body=None, else_body=None):
        self.target = target
        self.iter = iter
        self.body = body
        self.else_body = else_body
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"AsyncFor({self.target}, {self.iter}, {self.body}, {self.else_body})"


class AsyncWithItem:
    def __init__(self, target=None, value=None):
        self.target = target
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"AsyncWithItem({self.target}, {self.value})"


class Assign:
    def __init__(self, target=None, value=None):
        self.target = target
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Assign({self.target}, {self.value})"


class AugAssign:
    def __init__(self, target=None, op=None, value=None):
        self.target = target
        self.op = op
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"AugAssign({self.target}, {self.op}, {self.value})"


class AnnAssign:
    def __init__(self, target=None, annotation=None, value=None):
        self.target = target
        self.annotation = annotation
        self.value = value
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"AnnAssign({self.target}, {self.annotation}, {self.value})"
