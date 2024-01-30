from Compiler.Context import Context
from Compiler.Symbol import Var, TypeVar
import typing


class ContextManager:
    def __init__(self, defaultGlobal: Context = None):
        if defaultGlobal == None:
            self.contexts = self.globalContext = Context(
                dict()  # Default Gloabl Built-in Context
            )
        else:
            self.contexts = self.globalContext = defaultGlobal

        self.callChain = []  # G , G + a , G + a + b , G + a + b + c , G + a + b + c + d
        self.callHistory = []  # G, a, b, c, d
        self.latestContext = self.contexts  # G + a + b + c
        self.callChain.append(self.contexts)  # G + a + b + c + d
        self.currentContext = self.contexts  # G + a + b + c + d
        self.callHistory.append(self.currentContext)  # G , a, b, ,c, d

    def enter(self, c: Context = None):  # d
        if c != None:
            self.latestContext = self.callChain[-1]  # G + a + b + c
            self.callChain.append(
                current := self.currentContext + c
            )  # G + a + b + c + d
            self.currentContext = current  # G + a + b + c + d
            self.callHistory.append(c)  # G , a, b, ,c, d
        else:
            cN = Context(dict())  # d
            self.latestContext = self.callChain[-1]  # G + a + b + c
            self.callChain.append(
                current := self.currentContext + cN
            )  # G + a + b + c + d
            self.currentContext = current
            self.callHistory.append(cN)  # G , a, b, ,c, d

    def leave(self):
        self.callChain.pop()
        self.currentContext = self.latestContext
        self.latestContext = self.callChain[-1]
        return self.callHistory.pop()

    def __getitem__(self, name: str) -> typing.Any:
        return self.currentContext[name]

    # def __getattr__(self, name: str) -> typing.Any:
    #     return self.currentContext[name]

    def __setitem__(self, name: str, value: typing.Any) -> typing.Any:
        self.currentContext[name] = value
        self.callHistory[-1][name] = value
        return value

    # def __setattr__(self, name: str, value: typing.Any) -> typing.Any:
    #     self.currentContext[name] = value
    #     return value

    def setEnd(self, name: str, value: typing.Any) -> typing.Any:
        self.callHistory[-1][name] = value
        self.currentContext[name] = value
        return value

    def getEnd(self, name: str) -> typing.Any:
        return self.callHistory[-1][name]

    def setGlobal(self, name: str, value: typing.Any) -> typing.Any:
        self.globalContext[name] = value
        return value

    def getGlobal(self, name: str) -> typing.Any:
        return self.globalContext[name]

    def getTypedLocal(self, name: str) -> TypeVar:
        if name in self.currentContext and isinstance(
            self.currentContext[name], TypeVar
        ):
            return self.currentContext[name], self.currentContext[name].type
        else:
            raise Exception(f"Variable {name} is not a TypeVar")

    def setTypedLocal(self, name, value, checker):
        if checker(self.currentContext[name].type, value):
            self.currentContext[name] = value
        else:
            raise Exception(f"Type Error: {self.currentContext[name].type} != {value}")

    def getTypedGlobal(self, name: str) -> TypeVar:
        if name in self.globalContext and isinstance(self.globalContext[name], TypeVar):
            return self.globalContext[name], self.globalContext[name].type
        else:
            raise Exception(f"Variable {name} is not a TypeVar")

    def setTypedGlobal(self, name, value, checker):
        if checker(self.globalContext[name].type, value):
            self.globalContext[name] = value
        else:
            raise Exception(f"Type Error: {self.globalContext[name].type} != {value}")

    def __delitem__(self, name: str) -> typing.Any:
        del self.currentContext[name]

    # def __delattr__(self, name: str) -> typing.Any:
    #     del self.currentContext[name]

    def delGlobal(self, name: str) -> typing.Any:
        del self.globalContext[name]

    def __repr__(self) -> str:
        return f"ContextManager object: ContextManager({self.contexts})"

    def __str__(self) -> str:
        return str(self.contexts)

    def __contains__(self, name: str) -> bool:
        return name in self.currentContext

    def __iter__(self) -> typing.Iterator:
        return iter(self.currentContext)

    def __len__(self) -> int:
        return len(self.currentContext)

    def __add__(self, other: Context) -> Context:
        # Neeed to specify the meaning of two context manager addition : what is used for?
        return self.currentContext + other
