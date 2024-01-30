from Compiler.ContextManager import ContextManager as CM
from Compiler.Procedure import Procedure
import Compiler.Symbol as Symbol
from Compiler.OO import Class

import Grammer.Tokens as Tokens
import Grammer.BNF as bnf
import Grammer.TypingSys as tsys

import Debugger.built_in as built_in


# To Do, chain different Parser
def parser(ast, context: CM):
    match ast:
        case float(x) | int(x) | bool(x) | str(x) | dict(x) | list(x):  # Value
            return x
        ########################################
        #
        # Var object can be parse to itself
        # Variable is a token, not a symbol
        # Var can use implicitly
        # Variable always use explicitly
        #
        ########################################
        case (Tokens.Variable, str(x)):  # Symbol
            if x in context.currentContext:
                return context.currentContext[x]
            else:
                context[x] = None
            return context[x]
        case (Symbol.Var, x):
            #  (Var, 'x')
            return context[x]
        case (Tokens.Variable, x):
            # (Variable, 'x')
            return context[x]
        case (x) if isinstance(x, Symbol.Var):
            # x=Var('x')
            # (Var('x'))
            return context[x]
        case (Tokens.Assign, (Tokens.Variable, x), y):
            # (Assign, (Variable, 'x'), 1)
            context[x] = parser(y, context)
            return context[x]
        case (Tokens.Assign, x, y) if isinstance(
            x, Symbol.Var
        ):  # (Assign, Var('x'), 1)
            context[x] = parser(y, context)
            return context[x]
        ########################################
        #
        # Function defination
        # Syntax
        #
        # (FunctionDef, Name, (params), *body)
        #
        # Example
        #  (FunctionDef ,
        #        'f' , ('x', 'y') ,
        #        (Print, (Add, (Variable, 'x'), (Variable, 'y')))
        #    )
        #
        # Call
        # Syntax
        #  (Call, Name, *args)
        #
        # Example
        #  (Call, 'f', 1, 2)
        #
        ########################################
        case (Tokens.FunctionDef, bnf.Name(n), tuple(params), *body):
            # (FunctionDef , 'f' , ('x', 'y') , (Print, (Add, (Variable, 'x'), (Variable, 'y'))))
            context[n] = Procedure(n, params, body)
            # context[n+'.types'] = tsys.Callable( , name=n)
            return context[n]
        case (Tokens.Return, x):
            return parser(x, context)
        case (Tokens.Call, bnf.Name(n), *args):
            # (Call, 'f', 1, 2)
            return context[n].call(args, context, parser)

        ########################################
        #
        # Class defination
        #
        ########################################
        case (Tokens.ClassDef, bnf.Name(n), tuple(staticVars), tuple(methods)):
            # (ClassDef, 'A', (FunctionDef, 'f', ('x', 'y'), (Print, (Add, (Variable, 'x'), (Variable, 'y'))))))
            context[n] = Class(n)
            context[n].init(staticVars, methods, context, parser)
        case (Tokens.New, bnf.Name(n), *args):
            # (New, 'A', 1, 2)
            # objectName = context[n].createInstance(n, args, context, parser)
            tempObject = context[n].copy()
            objectName = tempObject.createInstance(n, args, context, parser)
            context[objectName] = tempObject
            return objectName
        case (Tokens.Delete, bnf.Name(n)):
            # (Delete, 'A')
            return context[n].deleteInstance(n, context, parser)

        ######
        #
        # Reset Built-in
        #
        #######
        case (Tokens.Print, x):
            print(parser(x, context))
            return None
        case (Tokens.Print, *x):
            print(*map(lambda x: parser(x, context), x))
            return None
        case (Tokens.Add, *x):
            return sum(map(lambda x: parser(x, context), x))
        case (Tokens.And, *x):
            return all(map(lambda x: parser(x, context), x))
        case (Tokens.Or, *x):
            return any(map(lambda x: parser(x, context), x))
        case (Tokens.Dict, x):
            return dict(x)
        case (Tokens.Divide, x, y):
            return parser(x, context) / parser(y, context)
        case (Tokens.FloorDivide, x, y):
            return parser(x, context) // parser(y, context)
        case (Tokens.GreaterThan, x, y):
            return parser(x, context) > parser(y, context)
        case (Tokens.GreaterThanEqual, x, y):
            return parser(x, context) >= parser(y, context)
        case (Tokens.In, x, y):
            return parser(x, context) in parser(y, context)
        case (Tokens.Is, x, y):
            return parser(x, context) is parser(y, context)
        case (Tokens.IsNot, x, y):
            return parser(x, context) is not parser(y, context)
        case (Tokens.LessThan, x, y):
            return parser(x, context) < parser(y, context)
        case (Tokens.LessThanEqual, x, y):
            return parser(x, context) <= parser(y, context)
        case (Tokens.List, *x):
            return list(x)
        case (Tokens.Modulo, x, y):
            return parser(x, context) % parser(y, context)
        case (Tokens.Multiply, *x):
            s = 1
            for i in x:
                s *= parser(i, context)
            return s
        case (Tokens.Not, x):
            return not parser(x, context)
        case (Tokens.NotEqual, x, y):
            return parser(x, context) != parser(y, context)
        case (Tokens.Set, x):
            return set(x)
        case (Tokens.String, *x):
            s = ""
            for i in x:
                s += parser(i, context)
            return s
        case (Tokens.Subtract, x, y):
            return parser(x, context) - parser(y, context)
        case (Tokens.Tuple, *x):
            return tuple(x)
        case _:
            return built_in.NoPatternMatched("No Pattern Matched")


def typeParser(ast, context: CM):
    match ast:
        # Built - in Constants
        case float(x):
            return x, tsys.TypedVariable("float", "float")
        case int(x):
            return x, tsys.TypedVariable("int", "int")
        case bool(x):
            return x, tsys.TypedVariable("bool", "bool")
        case str(x):
            return x, tsys.TypedVariable("str", "str")
        case dict(x):
            return x, tsys.TypedVariable("dict", "dict")
        case list(x):
            return x, tsys.TypedVariable("list", "list")

        #########################################################################
        # Variable Define
        #
        # General Access Variable
        case (Tokens.Variable, str(x)) | (Symbol.Var, x):
            if (
                x in context.currentContext
                and str(x) + ".types" in context.currentContext
            ):
                return context[x], context.currentContext[str(x) + ".types"]
            else:
                return context[x], built_in.UnknownType
        case (x) if isinstance(x, Symbol.Var):
            # x=Var('x')
            # (Var('x'))
            if (
                x in context.currentContext
                and str(x) + ".types" in context.currentContext
            ):
                return context[x], context.currentContext[str(x) + ".types"]
            else:
                return context[x], built_in.UnknownType

        # Set TypeThrough Assign
        # No Forced Type Check
        case (Tokens.Assign, (Tokens.Variable, x), y):
            # (Assign, (Variable, 'x'), 1)
            v, t = typeParser(y, context)
            context[x] = v
            context[x + ".types"] = t
            return v, t

        # Set TypeThrough Assign
        case (Tokens.Assign, x, y) if isinstance(
            x, Symbol.Var
        ):  # (Assign, TypeVar('x',t), 1)
            v, t = typeParser(y, context)
            # if context[x + ".types"] == t:
            context[x] = v
            context[x + ".types"] = t
            return v, t

        # The only ways to define type of variable
        case (Symbol.TypeVar, x, t) if isinstance(t, str):
            context[x] = None
            context[x + ".types"] = r = tsys.TypedVariable(x, t)
            x.type = r
            return None, r

        case (Symbol.TypeVar, x, t) if isinstance(t, tsys.TypedVariable):
            context[x] = None
            context[x + ".types"] = t
            x.type = t
            return None, t

        case (Symbol.TypeVar, x, Tokens.Auto, v):
            context[x], t = typeParser(v, context)
            context[x + ".types"] = t
            x.type = t
            return context[x], t
        
        case (Tokens.Auto, x, v):
            context[x], t = typeParser(v, context)
            context[x + ".types"] = t
            x.type = t
            return context[x], t

        case (x) if isinstance(x, Symbol.TypeVar):
            if (
                x in context.currentContext
                and str(x) + ".types" in context.currentContext
            ):
                # context[x] = None
                # context[x + ".types"] = x.type
                return context[x], x.type
            else:
                return None, x.type

        # Explicity Type Define
        case (Symbol.TypeName, x):
            return tsys.TypedVariable(x, x), tsys.TypedVariable(x, x)

        case (Tokens.Assign, x, y) if isinstance(
            x, Symbol.TypeVar
        ):  # (Assign, TypeVar('x'), 1)
            # Compulsary type check
            v, t = typeParser(y, context)
            # context[x] = v
            if context[x + ".types"] == t:
                context[x] = v
            else:
                raise RuntimeError(
                    "Type Mismatch {:} != {:}".format(context[x + ".types"], t)
                )
            return v, t

        case (Tokens.Assign, (Symbol.TypeVar, x), y):
            # Compulsary type check
            v, t = typeParser(y, context)
            # context[x] = v
            if context[x + ".types"] == t:
                context[x] = v
            else:
                raise RuntimeError(
                    "Type Mismatch {:} != {:}".format(context[x + ".types"], t)
                )
            return v, t

        #########################################################################
        # Function
        case (Tokens.FunctionDef, bnf.Name(n), tuple(params), *body):
            # (FunctionDef , 'f' , ('x', 'y') , (Print, (Add, (Variable, 'x'), (Variable, 'y'))))
            context[n] = Procedure(n, params, body)
            # context[n+'.types'] = tsys.Callable( , name=n)
            match params:
                case ():
                    return context[n], tsys.Callable([], n)
                case (x, *xs) if isinstance(x, Symbol.TypeVar):
                    return context[n], tsys.Callable(
                        [x.type] + list(map(lambda x: x.type, xs)), n
                    )
                case _:
                    return context[n], built_in.UnknownType

        # case (Tokens.FunctionDef, bnf.Name(n), tuple(params), *body):

        # case (Tokens.FunctionDef, bnf.Name(n), tuple(params), *body):
        #    # (FunctionDef , 'f' , ('x', 'y') , (Print, (Add, (Variable, 'x'), (Variable, 'y'))))
        #    context[n] = Procedure(n, params, body)
        #    # context[n+'.types'] = tsys.Callable( , name=n)
        #    return context[n], built_in.UnknownType
        case (Tokens.Return, x):
            return parser(x, context), built_in.UnknownType
        case (Tokens.Call, bnf.Name(n), *args):
            # (Call, 'f', 1, 2)
            return context[n].call(args, context, parser), built_in.UnknownType

        case _:
            return parser(ast, context), built_in.UnknownType








class Parser:
    def __init__(self, context: CM) -> None:
        self.context = context

    def parse(self, ast):
        return parser(ast, self.context)

    def typeParse(self, ast):
        return typeParser(ast, self.context)
