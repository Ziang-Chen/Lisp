from Compiler.ContextManager import ContextManager as CM
from Compiler.Context import Context
from Compiler.Procedure import Procedure
import typing
from Compiler.Symbol import Var, TypeVar
import contextlib
import copy


@contextlib.contextmanager
def enterContext(env: CM, context: Context):
    env.enter(context)
    try:
        yield env
    finally:
        env.leave()


class Class:
    # def __init__(self, name, staticVars: dict, methods: typing.List[Procedure]):
    #     # Store Type Name
    #     self.name = name
    #     # Initiliaze Inner Context
    #     self.context = Context()
    #     self.methods = methods
    #     for k, value in staticVars:
    #         self.context[k] = value
    #     for method in methods:
    #         self.context[method.name] = method

    def __init__(self, name, context: Context = None):
        self.name = name
        if context == None:
            self.context = Context()
        self.context = context

    def initOnlyBody(self, body, env: CM, parser):
        env.enter(self.context)
        for i in body:
            parser(i, env, parser)
        self.context = env.leave()

    def init(self, vars, methods, env: CM, parser):
        env.enter(self.context)
        for var in vars:
            parser(var, env, parser)
        for method in methods:
            parser(method, env, parser)
        env.leave()

    def copy(self):
        # return Class(self.name, copy.deepcopy(self.context.content), self.methods)
        return Class(self.name, copy.deepcopy(self.context))

    def createInstance(self, name, args, env: CM, parser):
        # call construct method, and return instance TypeVar
        self.args = args
        if "init" in self.context:
            # with enterContext(env, self.context) as e:
            #    self.context["init"].call(args, e, parser)
            env.enter(self.context)
            self.context["init"].call(args, env, parser)
            env.leave()
            return TypeVar(name, self.name)
        else:
            raise Exception("No init method found")

    def deleteInstance(self, name, env: CM, parser):
        if "del" in self.context:
            # with enterContext(env, self.context) as e:
            #    self.context["del"].call(self.args, e, parser)
            env.enter(self.context)
            self.context["del"].call(self.args, env, parser)
            env.leave()
        else:
            raise Exception("No del method found")

    def accessAttribute(self, attr):
        if attr in self.context:
            return self.context[attr]
        else:
            raise Exception("No attribute found")

    def setAttribute(self, attr, value):
        if attr in self.context:
            self.context[attr] = value
            return value
        else:
            raise Exception("No attribute found")

    def callMethod(self, name, args, env: CM, parser):
        if name in self.context:
            with enterContext(env, self.context) as e:
                if args == None:
                    r = self.context[name].callWithoutArgs(e, parser)
                else:
                    r = self.context[name].call(args, e, parser)
            return r
            # env.enter(self.context)
            # self.context[name].call(args, env, parser)
            # env.leave()
        else:
            raise Exception("No method found")
