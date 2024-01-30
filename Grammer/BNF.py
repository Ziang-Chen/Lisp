from typing import Any, TypeAlias, NoReturn
from Compiler.Symbol import Var
from Compiler.Context import Context
from Compiler.ContextManager import ContextManager
#from Grammer.Tokens import *

Name: TypeAlias = str

"""
symbol: TypeAlias = Var
name: TypeAlias = Name
value: TypeAlias = float | int | bool | str | dict | list
atomic: TypeAlias = value | symbol | name
expression: TypeAlias = atomic | tuple[atomic, ...]


assign_expression: TypeAlias = tuple[Assign, symbol, expression]
return_expression: TypeAlias = tuple[Return, expression]
print_expression: TypeAlias = tuple[Print, expression]

if_expression: TypeAlias = tuple[expression, expression, expression]
while_expression: TypeAlias = tuple[expression, expression]
for_expression: TypeAlias = tuple[expression, expression, expression]
function: TypeAlias = tuple[tuple[name, ...], expression]
"""
