# AtomicPy

Symbolic Way to Embed Lisp Style Language in Python

Author: Ziang Chen

```python
import Tools.pyEmbed as pebd
from Grammer.Tokens import *
from Compiler.Symbol import Var, TypeVar, TypeName

g= pebd.createEnv("parserv3") #Specify Parser

# Yes, After import & initialization
# Following lines can run in Python Interpreter
g @ (                    # Class Definition
    ClassDef,
    "Point",             # Class Name
    (Var, "self.x", 0),  # Initial List
    (Var, "self.y", 0),
    (
        FunctionDef,     # Construct Method
        "init",
        ((TypeVar, "x", "int"), 
        (TypeVar, "y", "int")),
        (Assign, (Var, "self.x"), (Var, "x")),
        (Assign, (Var, "self.y"), (Var, "y")),
    ),
    (FunctionDef, "printx", 
     None, 
     (Print, (Variable, "self.x"))
     ),
    (FunctionDef, "setx",
        ((Variable, 'x'),), 
        (Assign, (Var, "self.x"), (Var, "x"))),
)

g@ (Assign, 'x', (New, "Point", 1,2)) # Create Object
g@ (Call, ('x','printx')) # Output: 1
g@(Call,  ('x','setx'), 10) 
g@(Call, ('x','printx')) # Output: 10
```

## Variable

A variable is a symbol, which aslo treated as a key in Context, used to mappying to a value. 

Initially, like evry language, gloable/standard Context is defined, after enter blocks/ class/ object/ function, new context will entered, and variable will store in the new context.

AtomicPy implete two types of variable, called typed variable and untyped variable. Assign operator also check types explicilty when left value is typed variable, otherwise it will be treated as untyped variable, but type will still stored in compiler for hints/optimization.

```Lisp
Syntax

Access Variable
    (x,) 

Declare Variable/ Access when Using Assign 
    VarDef :=([Var|Variable], NameString [, value])                            

Define Type                 
    TypeDef:=(TypeName, [NameString|type] [,value])              

Define Typed Variable
    TypeVarDef:=(TypeVar, NameString, [TypeString|Type], [,value])                 

Assign Value to Variable
    (Assign, [NameString|VarDef|TypeVarDef] , [Value|Expression])  

Example
    (x,)
    (Var, 'x') | (Variable, 'x')         
    (Var, 'x', 1) | (Variable, 'x', 1)    
    (TypeVar, 'x', 'int')                 
    (TypeVar, 'x', 'int', 1)              
    (TypeName, 'int')                     
    (TypeName, 'int', 1)  //  Anonymous Typed Variable (Constant)
    (Assign, (Var, 'x'), 1)              
    (Assign, (TypeVar, 'x', 'int'), 1)    
    (Assign, x=Var('x'), 1)              
    (Assign, x=TypeVar('x', 'int'), 1)    
    (Assign, (Var, 'x'), y)             
    (Assign, (TypeVar, 'x', 'int'), y)   
    (Assign, x, y)                        
```
Type also can be used in more elgent way, like
```python
String = (g@("ConstantString")).Type # Define Type of String
Float = (g@(1.23456)).Type           # Define Type of Float
g@(Assign,  (TypeVar, 'x', Float), 1.0)
```

Notic the return value if g@, highly related to syntax tree parser, which basically contains all neccessary inofrmation for AtomicPy.

## Function

Function is a procedure, can be called with arguments. Function can be defined in two ways, using FunctionDef, or using Lambda.

```Lisp
(FunctionDef, NameString, [ArgList|None], Expression)
(Lambda, [ArgList|None], Expression)
```
## Class

Class is a type, each object initialized from a class by method "init"

Method call be called using following syntax
``` python
g@ (Call, (ObjectName, MethodName), *args)
g@(Call, (ObjectName, MethodName))
```