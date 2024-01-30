from typing import Any
from Compiler.ContextManager import ContextManager as CM
from Compiler.Procedure import Procedure
import Compiler.Symbol as Symbol
from Compiler.OO import Class

import Grammer.Tokens as Tokens
import Grammer.BNF as bnf
import Grammer.TypingSys as tsys

import Debugger.built_in as built_in
import functools


class parserReturnType:
    def __init__(self, context, value=None, var=None, callable=None, Type=None):
        # Update & Passing Context Through Different Parser is compulsory
        # For better clearity &
        # Safety
        self.value = value
        self.var = var
        self.context = context
        self.callable = callable
        self.Type = Type

    def isVar(self):
        return self.var

    def isTyped(self):
        return self.Type

    def isCallable(self):
        return self.callable

    def __str__(self) -> str:
        return f"parserReturnType:\n\tvalue: {self.value} \n\tvar: {self.var} \n\ttype: {self.Type} \n\tcallable: {self.callable}"

    def __repr__(self) -> str:
        return f"parserReturnType:\n\tvalue: {self.value} \n\tvar: {self.var} \n\ttype: {self.Type} \n\tcallable: {self.callable}"


def atomicParser(ast, context: CM, parser=None) -> parserReturnType:
    # Syntax

    # (x,)                                                 -> value
    # (Var, NameString) | (Variable, NameString)          ->    var
    # (Var, NameString, Value) | (Variable, NameString, Value)    -> value
    # (TypeName, NameString|type ,value)                       -> value
    # (TypeName, NameString [, value])                             -> type/value
    # (TypeVar, NameString, TypeString)                  -> typevar
    # (TypeVar, NameString, TypeString, Value)           -> value
    # (TypeVar, NameString, Type [,value])                 -> var/value

    # (Assign, [(Variable|Var), NameString]|Var|TypedVar , Value)     -> value

    # Example
    # ('x',)
    # (Var, 'x') | (Variable, 'x')          -> var
    # (Var, 'x', 1) | (Variable, 'x', 1)    -> value
    # (TypeVar, 'x', 'int')                  -> typevar
    # (TypeVar, 'x', 'int', 1)               -> typevar
    # (TypeName, 'int')                     -> type
    # (TypeName, 'int', 1)                  -> value
    #                    Anonymous Typed Variable: Constant
    # (Assign, (Var, 'x'), 1)                -> value
    # (Assign, (TypeVar, 'x', 'int'), 1)    -> value
    # (Assign, x=Var('x'), 1)               -> value
    # (Assign, x=TypeVar('x', 'int'), 1)     -> value
    # (Assign, (Var, 'x'), y)               -> value
    # (Assign, (TypeVar, 'x', 'int'), y)    -> value
    # (Assign, x, y)                        -> value

    match ast:
        # Only Access
        #
        #   Context Only Store Reference of Specific Type of Variable
        #   In other Words
        #
        #       Context[x] = Var(x)/TypeVar(x)/TypeName(x)
        #       Context[x].value = value
        #       Context[x].type = type
        #
        #

        # (x,)                                -> value
        case (x,) if isinstance(x, Symbol.Var):
            if not str(x) + ".type" in context.currentContext:
                return parserReturnType(var=x, value=context[x].value, context=context)
            else:
                return parserReturnType(
                    var=x,
                    Type=context.currentContext[str(x) + ".type"],
                    value=context[x].value,
                    context=context,
                )

        # (Var, 'x') | (Variable, 'x')          -> var
        # Access or Define
        case (Tokens.Variable, x) | (Symbol.Var, x):
            if not x in context.currentContext:
                x_ = Symbol.Var(x)
                context[x] = x_
                return parserReturnType(var=context[x], context=context)
            if not str(x) + ".type" in context.currentContext:
                return parserReturnType(
                    var=context[x], value=context[x].value, context=context
                )
            else:
                return parserReturnType(
                    var=context[x],
                    Type=context.currentContext[str(x) + ".type"],
                    value=context[x].value,
                    context=context,
                )

        # (Var, 'x', 1) | (Variable, 'x', 1)    -> value
        # Define Only
        case (Tokens.Variable, x, y) | (Symbol.Var, x, y):
            context[x] = Symbol.Var(x, y)
            context[x].value = atomicParser(y, context, parser).value
            return parserReturnType(value=y, var=context[x], context=context)

        # (TypeVar, 'x', 'int')                  -> typevar
        # Define only
        case (Symbol.TypeVar, x, y) if isinstance(y, str):
            t = tsys.TypedVariable(name=x, type=tsys.TypedBase(y))
            context[x] = Symbol.TypeVar(x, t)
            context[str(x) + ".type"] = t
            return parserReturnType(var=context[x], Type=t, context=context)

        # (TypeVar, 'x', 'int', 1)               -> typevar
        # Define only
        case (Symbol.TypeVar, x, y, z) if isinstance(y, str):
            t = tsys.TypedVariable(name=x, type=tsys.TypedBase(y))
            context[x] = Symbol.TypeVar(x, t)
            context[x].value = atomicParser(z, context, parser).value
            context[str(x) + ".type"] = t
            return parserReturnType(
                var=context[x], Type=t, value=context[x].value, context=context
            )
        # (TypeName, type)                      -> type
        case (Symbol.TypeName, x) if isinstance(x, tsys.TypedBase):
            return parserReturnType(Type=x, context=context)

        # (TypeName, 'int')                     -> type
        case (Symbol.TypeName, x) if isinstance(x, str):
            t = tsys.TypedBase(x)
            return parserReturnType(Type=t, context=context)

        # (TypeName, 'int', 1)                  -> value
        case (Symbol.TypeName, x, y) if isinstance(x, str):
            t = tsys.TypedBase(x)
            parsed = atomicParser(y, context, parser)
            if parsed.Type == t:
                return parserReturnType(value=y, Type=t, context=context)
            else:
                raise Exception(f"Type Error: {t} != {parsed.Type}")

        # (TypeName ,type, value)               -> value
        case (Symbol.TypeName, x, y) if isinstance(x, tsys.TypedBase):
            parsed = atomicParser(y, context, parser)
            if parsed.Type == x:
                return parserReturnType(value=y, Type=x, context=context)
            else:
                raise Exception(f"Type Error: {x} != {parsed.Type}")

        # (TypeVar, 'x', Type [,value])                 -> var/value
        # Define Only
        case (Symbol.TypeVar, x, y) if isinstance(y, tsys.TypedBase):
            t = y
            context[x] = Symbol.TypeVar(x, t)
            context[str(x) + ".type"] = t
            return parserReturnType(var=context[x], Type=t, context=context)

        # (TypeVar, 'x', Type ,value)                 -> value
        # Assign using type check
        case (Symbol.TypeVar, x, y, z) if isinstance(y, tsys.TypedBase):
            t = y
            context[x] = Symbol.TypeVar(x, t)
            context[str(x) + ".type"] = t
            r = atomicParser(z, context, parser)

            if context[x].type == r.Type:
                context[x].value = r.value
                context[str(x) + ".type"] = y
                return parserReturnType(
                    var=context[x], Type=y, value=r.value, context=context
                )
            else:
                raise Exception(f"Type Error: {y} != {r.Type}")

        # (TypeVar, 'x', TypeStr ,value)                 -> value
        # Assign with type check
        case (Symbol.TypeVar, x, y, z) if isinstance(y, str):
            t = tsys.TypedBase(y)
            context[x] = Symbol.TypeVar(x, t)
            context[str(x) + ".type"] = t
            r = atomicParser(z, context, parser)
            if context[x].type == r.Type:
                context[x].value = r.value
                context[str(x) + ".type"] = y
                return parserReturnType(
                    var=context[x], Type=y, value=r.value, context=context
                )
            else:
                raise Exception(f"Type Error: {y} != {r.Type}")

        # (TypeVar, 'x', TypeStr ,value)                 -> variable
        # Define Only
        case (Symbol.TypeVar, x, y) if isinstance(y, str):
            t = tsys.TypedBase(y)
            context[x] = Symbol.TypeVar(x, t)
            context[str(x) + ".type"] = t
            return parserReturnType(var=context[x], Type=t, context=context)

        # (Assign, [(Variable|Var), NameString]|Var|TypedVar , Value)     -> value
        # (Assign, LeftValue, RightValue)
        case (Tokens.Assign, x, y):
            if isinstance(x, Symbol.Var):
                context[x.name] = x
                context[x.name].value = atomicParser(y, context, parser).value
                return parserReturnType(
                    var=context[x], value=context[x].value, context=context
                )
            # elif isinstance(x, Symbol.TypeVar):
            #     context[x.name] = x
            #     context[x.name].value = atomicParser(y, context, parser).value
            #     context[str(x.name) + ".type"] = x.type
            #     return parserReturnType(
            #         var=context[x],
            #         Type=context[x].type,
            #         value=context[x].value,
            #         context=context,
            #     )
            elif isinstance(x, str):
                context[x] = Symbol.Var(x)
                context[x].value = atomicParser(y, context, parser).value
                return parserReturnType(
                    var=context[x], value=context[x].value, context=context
                )
            else:
                match x:
                    case (Tokens.Variable, x):
                        context[x] = Symbol.Var(x)
                        context[x].value = atomicParser(y, context, parser).value
                        return parserReturnType(
                            var=context[x], value=context[x].value, context=context
                        )
                    # case (Symbol.TypeVar, x, y):
                    #     context[x] = Symbol.TypeVar(x, y)
                    #     context[x].value = atomicParser(y, context, parser).value
                    #     context[str(x) + ".type"] = y
                    #     return parserReturnType(
                    #         var=context[x],
                    #         Type=context[x].type,
                    #         value=context[x].value,
                    #         context=context,
                    #    )
                    case _:
                        pass

            parsed_x = atomicParser(x, context, parser)
            parsed_y = atomicParser(y, parsed_x.context, parser)
            context = parsed_y.context
            if parsed_x.isVar():
                if parsed_x.isTyped():
                    if context[parsed_x.var.name].type == parsed_y.Type:
                        context[parsed_x.var.name].value = parsed_y.value
                        return parserReturnType(
                            value=parsed_y.value, Type=parsed_y.Type, context=context
                        )
                    else:
                        raise Exception(
                            f"Type Error: {parsed_x.Type} != {parsed_y.Type}"
                        )
                else:
                    context[parsed_x.var.name].value = parsed_y.value
                    context[str(parsed_x.var.name) + ".type"] = parsed_y.Type
                    return parserReturnType(
                        value=parsed_y.value, context=context, Type=parsed_y.Type
                    )

            else:
                raise Exception(f"Can't assign to {x}")

        #######################
        # int
        # float
        # bool
        # str
        # dict
        # list
        # (Print, x)
        # (Print, *x)
        # (Add, *x)
        # (And, *x)
        # (Or, *x)
        # (Dict, x)
        # (Divide, x, y)
        # (FloorDivide, x, y)
        # (GreaterThan, x, y)
        # (GreaterThanEqual, x, y)
        # (In, x, y)
        # (Is, x, y)
        # (IsNot, x, y)
        # (LessThan, x, y)
        # (LessThanEqual, x, y)
        # (List, *x)
        # (Modulo, x, y)
        # (Multiply, *x)
        # (Not, x)
        # (NotEqual, x, y)
        # (Set, x)
        # (String, *x)
        # (Subtract, x, y)
        # (Tuple, *x)
        ##########################

        case int(x):
            return parserReturnType(
                value=x, Type=tsys.TypedBase("int"), context=context
            )
        case float(x):
            return parserReturnType(
                value=x, Type=tsys.TypedBase("float"), context=context
            )
        case bool(x):
            return parserReturnType(
                value=x, Type=tsys.TypedBase("bool"), context=context
            )
        case str(x):
            return parserReturnType(
                value=x, Type=tsys.TypedBase("str"), context=context
            )
        case dict(x):
            return parserReturnType(
                value=x, Type=tsys.TypedBase("dict"), context=context
            )
        case list(x):
            return parserReturnType(
                value=x, Type=tsys.TypedBase("list"), context=context
            )
        case (Tokens.Print, x):
            print(atomicParser(x, context).value)
            return parserReturnType(context=context)
        case (Tokens.Print, *x):
            print(*map(lambda x: atomicParser(x, context).value, x))
            return parserReturnType(context=context)
        case (Tokens.Add, *x):
            return parserReturnType(
                value=sum(map(lambda x: atomicParser(x, context).value, x)),
                context=context,
            )
        case (Tokens.And, *x):
            return parserReturnType(
                value=all(map(lambda x: atomicParser(x, context).value, x)),
                context=context,
            )
        case (Tokens.Or, *x):
            return parserReturnType(
                value=any(map(lambda x: atomicParser(x, context).value, x)),
                context=context,
            )
        case (Tokens.Dict, x):
            return parserReturnType(context=context, value=dict(x))
        case (Tokens.Divide, x, y):
            return parserReturnType(
                context=context,
                value=atomicParser(x, context).value / atomicParser(y, context).value,
            )
        case (Tokens.FloorDivide, x, y):
            return parserReturnType(
                context=context,
                value=atomicParser(x, context).value // atomicParser(y, context).value,
            )
        case (Tokens.GreaterThan, x, y):
            return parserReturnType(
                context=context,
                value=atomicParser(x, context).value > atomicParser(y, context).value,
            )
        case (Tokens.GreaterThanEqual, x, y):
            return parserReturnType(
                context=context,
                value=atomicParser(x, context).value >= atomicParser(y, context).value,
            )
        case (Tokens.In, x, y):
            return parserReturnType(
                context=context,
                value=atomicParser(x, context).value in atomicParser(y, context).value,
            )
        case (Tokens.Is, x, y):  #### Need to Redefined
            return atomicParser(x, context) is atomicParser(y, context)
        case (Tokens.IsNot, x, y):  ####
            return atomicParser(x, context) is not atomicParser(y, context)
        case (Tokens.LessThan, x, y):
            return parserReturnType(
                context=context,
                value=atomicParser(x, context).value < atomicParser(y, context).value,
            )
        case (Tokens.LessThanEqual, x, y):
            return parserReturnType(
                context=context,
                value=atomicParser(x, context).value <= atomicParser(y, context).value,
            )
        case (Tokens.List, *x):
            return parserReturnType(
                context=context,
                value=list(map(lambda x: atomicParser(x, context).value, x)),
            )
        case (Tokens.Modulo, x, y):
            return parserReturnType(
                context=context,
                value=atomicParser(x, context).value % atomicParser(y, context).value,
            )
        case (Tokens.Multiply, *x):
            s = 1
            for i in x:
                s *= atomicParser(i, context).value
            return parserReturnType(context=context, value=s)
        case (Tokens.Not, x):
            return parserReturnType(
                context=context, value=not atomicParser(x, context).value
            )
        case (Tokens.NotEqual, x, y):
            return parserReturnType(
                context=context,
                value=atomicParser(x, context).value != atomicParser(y, context).value,
            )
        case (Tokens.Set, x):
            return parserReturnType(context=context, value=set(x))
        case (Tokens.String, *x):
            s = ""
            for i in x:
                s += atomicParser(i, context).value
            return parserReturnType(context=context, value=s)
        case (Tokens.Subtract, x, y):
            return parserReturnType(
                context=context,
                value=atomicParser(x, context).value - atomicParser(y, context).value,
            )
        case (Tokens.Tuple, *x):
            return parserReturnType(context=context, value=tuple(x))
        case (Tokens.Map, x, y):
            return parserReturnType(
                context=context,
                value=map(
                    lambda yi: atomicParser((Tokens.Call, x, yi), context).value,
                    y,
                ),
            )

        #############################################
        #
        #
        # parse Block
        #
        # Syntax
        # (Block, *body) -> last value in body
        # (If , condition, *body) -> last value in body
        # (If , condition, *body, Else, *elseBody) -> last value in body/elseBody
        # (While, condition, *body) -> last value in body
        # (For, var, iterable, *body) -> last value in body
        #
        # Example
        # (Block, (Var, 'x', 1), (Var, 'y', 2), (Add, (Var, 'x'), (Var, 'y'))) -> 3
        # (If, (GreaterThan, (Var, 'x'), (Var, 'y')), (Print, (Var, 'x')), (Print, (Var, 'y'))) -> 2
        # (If, (GreaterThan, (Var, 'x'), (Var, 'y')), (Print, (Var, 'x')), (Print, (Var, 'y')), Else, (Print, (Var, 'y')), (Print, (Var, 'x'))) -> 2
        # (While, (LessThan, (Var, 'x'), 10), (Print, (Var, 'x')), (Assign, (Var, 'x'), (Add, (Var, 'x'), 1)))) -> 10
        # (For, 'x', (Range, 10), (Print, (Var, 'x'))) -> 9
        #
        #
        #
        #############################################

        case (Tokens.Block, *body):
            context.enter()
            for i in body:
                r = atomicParser(i, context, parser)
                context = r.context
            context.leave()
            return r
        case (Tokens.If, condition, singleLine):
            r = atomicParser(condition, context, parser)
            if r.value:
                # for i in body:
                r = atomicParser(singleLine, context, parser)
                context = r.context
                return r
            else:
                return r
        case (Tokens.If, condition, a, Tokens.Else, b):
            r = atomicParser(condition, context, parser)
            if r.value:
                r = atomicParser(a, context, parser)
                return r
            else:
                r = atomicParser(b, context, parser)
                context = r.context
                return r
        case (Tokens.While, condition, *body):
            while atomicParser(condition, context, parser).value:
                for i in body:
                    r = atomicParser(i, context, parser)
                    context = r.context
                return r
        case (Tokens.For, var, iterable, body):
            for i in iterable:
                # context[var] = Symbol.Var(var, i)
                atomicParser((Tokens.Assign, var, i), context, parser)
                r = atomicParser(body, context, parser)
                context = r.context
                return r

        ########################
        #
        # Function defination
        #
        #
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
        #
        #
        # Syntax
        #  (Call, Name, *args)
        #
        # Example
        #  (Call, 'f', 1, 2)
        #
        #########################

        # (FunctionDef, Name, None, *body)
        # Need to transfer context[n] = TypeVar(n, Callable, Procedure)
        case (Tokens.FunctionDef, bnf.Name(n), None, *body):
            # (FunctionDef , 'f' , None , (Print, (Add, (Variable, 'x'), (Variable, 'y'))))
            context[n] = Procedure(n, None, body)
            return parserReturnType(context=context, callable=context[n])

        case (Tokens.Call, bnf.Name(n)):
            return parserReturnType(
                context=context, value=context[n].callWithoutArgs(context, parser)
            )

        # (FunctionDef, Name, (params), *body)
        case (Tokens.FunctionDef, bnf.Name(n), tuple(params), *body):
            # (FunctionDef , 'f' , ('x', 'y') , (Print, (Add, (Variable, 'x'), (Variable, 'y'))))
            context[n] = Procedure(n, params, body)
            return parserReturnType(context=context, callable=context[n])
        # (Return, x)
        case (Tokens.Return, x):
            return parserReturnType(
                context=context, value=atomicParser(x, context, parser).value
            )
        # (Call, Name, *args)
        case (Tokens.Call, bnf.Name(n), *args):
            # (Call, 'f', 1, 2)
            return parserReturnType(
                context=context, value=context[n].call(args, context, parser)
            )

        # (Lambda, (params), *body)
        case (Tokens.Lambda, tuple(params), *body):
            return parserReturnType(
                context=context, callable=Procedure("lambda", params, body)
            )

        #########################
        #
        # Class Defination
        #
        # Syntax
        #
        # (ClassDef,
        #        Name,
        #        (Initia lists),
        #        (methods))
        #
        # (ClassDef,
        #        Name,
        #        Body) -> Body = (Initia lists) + (methods)
        #
        # Example
        # (ClassDef,
        #        'Point',
        #        (Var, 'x', 0), (Var, 'y', 0),
        #        (FunctionDef, 'init', ('self', 'x', 'y'), (Assign, (Var, 'self.x'), (Var, 'x')), (Assign, (Var, 'self.y'), (Var, 'y'))),
        #        (FunctionDef, 'move', ('self', 'x', 'y'), (Assign, (Var, 'self.x'), (Add, (Var, 'self.x'), (Var, 'x'))), (Assign, (Var, 'self.y'), (Add, (Var, 'self.y'), (Var, 'y')))))
        #
        #

        # (ClassDef, Name ,body)
        case (Tokens.ClassDef, bnf.Name(n), *body):
            # (ClassDef, 'A', (FunctionDef, 'f', ('x', 'y'), (Print, (Add, (Variable, 'x'), (Variable, 'y'))))))
            context[n] = Symbol.TypeVar(n, tsys.TypedBase(n), Class(n))
            context[n].value.initOnlyBody(body, context, parser)
            return parserReturnType(
                context=context, Type=context[n].type, var=context[n]
            )

        # (ClassDef, Name, (Initia lists), (methods))
        case (Tokens.ClassDef, bnf.Name(n), tuple(staticVars), tuple(methods)):
            # (ClassDef, 'A', (FunctionDef, 'f', ('x', 'y'), (Print, (Add, (Variable, 'x'), (Variable, 'y'))))))
            context[n] = Symbol.TypeVar(n, tsys.TypedBase(n), Class(n))
            context[n].init(staticVars, methods, context, parser)
            return parserReturnType(context=context, Type=context[n].type)

        # (New, Name, *args)
        case (Tokens.New, bnf.Name(n), *args):
            # (New, 'A', 1, 2)
            tempObject = context[n].value.copy()
            tmpobj = tempObject.createInstance(
                n, args, context, parser
            )  # return abondoned TypeVar
            return parserReturnType(
                context=context,
                value=tempObject,
                Type=context[n].type,
            )

        # (Call, (ObjectName, MethodName))
        case (Tokens.Call, tuple(names)):
            # (Call, 'a', 'f')
            return parserReturnType(
                context=context,
                value=context[names[0]].value.callMethod(
                    names[1], None, context, parser
                ),
            )

        # (Call, (ObjectName, MethodName), *args)
        case (Tokens.Call, tuple(names), *args):
            # (Call, 'a', 'f', 1, 2)
            value = context[names[0]].value.callMethod(names[1], args, context, parser)
            return parserReturnType(
                context=context,
                value=value,
            )

        # ((Lambda/FunctionDef/ClassDef/Type, ...), *args)  -> value
        case (x, *args):
            parsed_x = atomicParser(x, context, parser)
            context = parsed_x.context
            parsed_args = tuple(
                map(lambda x: atomicParser(x, context, parser).value, args)
            )
            if parsed_x.isCallable():
                return parserReturnType(
                    value=parsed_x.callable.call(parsed_args, context, parser),
                    context=context,
                )
            else:
                raise Exception(f"Can't call {x}")

        case _:
            if parser != None:
                return parser(ast, context, parser=atomicParser)
            else:
                raise Exception("Parser Error: No Pattern Matched")


def parse(ast, context: CM) -> parserReturnType:
    return atomicParser(ast, context, atomicParser)
