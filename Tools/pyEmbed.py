from Compiler.Context import Context
import Compiler.Symbol as Symbol
import typing
from Compiler.ContextManager import ContextManager
import Grammer.Tokens as Tokens
import operator as op
import Grammer.BNF as bnf
import Grammer.Sematics as sem
from Parser.lispStyle import parser


class pyEnv:
    def __init__(self):
        # Initial Built-in Function Bound
        self.globalContext = Context(sem.defaultOperation)
        # Initialized Global Context
        self.contextManager = ContextManager(self.globalContext)

    def parseLocal(self, ast):
        self.contextManager.enter()
        r = self.parse(ast)
        self.contextManager.leave()
        return r

    def parseGlobal(self, ast):
        return self.parse(ast)

    def parse(self, ast):
        return parser(ast, self.contextManager)


class envAccess:
    def __init__(self, env: pyEnv):
        self.env = env

    def __add__(self, other):
        return self.env.parseLocal(other)

    def __matmul__(self, other):
        return self.env.parseGlobal(other)


class createEnv:
    def __init__(self, parser="lispStyle"):
        # Initial Built-in Function Bound
        self.globalContext = Context(sem.defaultOperation)
        # Initialized Global Context
        self.contextManager = ContextManager(self.globalContext)
        self.parserText = parser

    def parseLocal(self, ast):
        self.contextManager.enter()
        r = self.parse(ast)
        self.contextManager.leave()
        return r

    def parseGlobal(self, ast):
        return self.parse(ast)

    def parse(self, ast):
        if self.parserText == "lispStyle":
            from Parser.lispStyle import parser

            return parser(ast, self.contextManager)
        elif self.parserText == "parserv3":
            from Parser.parserv3 import parse

            return parse(ast, self.contextManager)

    def __add__(self, other):
        return self.parseLocal(other)

    def __matmul__(self, other):
        return self.parseGlobal(other)
