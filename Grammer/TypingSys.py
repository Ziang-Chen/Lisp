# Built in optional Type system
import typing


"""
TypeVariable:
    Name:Type =Value # Value Store in Context/ContextManager Class

Composite Type:
    ClassType: Name = ClassType(Name, vars, methods)

Callable:
    Callable: Name = Callable(Name, returnType, params)

"""


class TypedBase:
    # type base class
    # only record type name
    def __init__(self, type) -> None:
        self.type = type

    def __repr__(self) -> str:
        return f"TypedVariable object: TypedVariable( {self.type})"

    def __hash__(self) -> int:
        return hash(self.type)

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if isinstance(other, TypedBase):
            return self.type == other.type
        else:
            return self.type == other
        # return self.type == other.type


class DerivedChain:
    # DerivedChain Class
    # Using For record Derived Chain
    def __init__(self, types) -> None:
        self.types = types

    def __repr__(self) -> str:
        return f"DerivedChain object: DerivedChain({self.types})"

    def __hash__(self) -> int:
        return hash(self.types)

    def contains(self, other):
        for t in self.types:
            if t == other:
                return True
        return False


class TypedVariable:
    def __init__(
        self, name, type: TypedBase = None, derivedChain: DerivedChain = None
    ) -> None:
        # Recommand type name always equal to name
        if type is None:
            self.type = TypedBase(name)
            self.name = name
        else:
            self.type = type
            self.name = name

        if derivedChain == None:
            self.derivedChain = []
        else:
            self.derivedChain = derivedChain

    def __repr__(self) -> str:
        return f"TypedVariable object: TypedVariable({self.name}, {self.type}), From {self.derivedChain}"

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if self.type == other.type:
            return True
        for derived in self.derivedChain:
            if derived == other:
                return True
        return False


class OptionalTypedVariable:
    def __init__(
        self, name, type: TypedBase = None, derivedChain: DerivedChain = None
    ) -> None:
        if type is None:
            self.type = TypedBase(name)
            self.name = name
        else:
            self.type = type
            self.name = name

        if derivedChain == None:
            self.derivedChain = []
        else:
            self.derivedChain = derivedChain

    def __repr__(self) -> str:
        return f"TypedVariable object: TypedVariable({self.name}, {self.type}), From {self.derivedChain}"

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other) -> bool:
        # Due to Optional Type
        # Type Checking Always Pass
        return True


class Callable:
    def __init__(self, typeList, name=None) -> None:
        # (returnType, *params )
        #
        self.typeList = typeList
        self.name = name

    def __repr__(self) -> str:
        return f"Callable object: Callable({self.typeList})"

    def __hash__(self) -> int:
        return hash(self.typeList)

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if self.typeList == other.typeList:
            return True
        return False


class ClassType:
    def __init__(self, name, vars, methods, derivedChain=None) -> None:
        self.name = name
        self.vars = vars
        self.methods = methods
        self.type = TypedVariable(self.name, derivedChain=derivedChain)
        self.derivedChain = derivedChain if derivedChain else []

    def hasMethod(self, name):
        for method in self.methods:
            if method.name == name:
                return method
        return False

    def __repr__(self) -> str:
        return f"ClassType object: ClassType({self.name}, {self.vars}, {self.methods})"

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other) -> bool:
        # Class Type is exactly the same Type
        if other is None:
            return False
        if self.name == other.name:
            # Goose Typing
            return True
        if self.type == other.type:
            return True
        if self.vars == other.vars and self.methods == other.methods:
            # Duck Typing
            return True
        return False

    def isDerived(self, other):
        # If Derived from other
        if self.type == other.type:
            return True
        return False

    def isInstance(self, other):
        # The most tolerant type checking
        if isinstance(other, ClassType):
            return self == other
        if isinstance(other, TypedVariable):
            return self.isDerived(other)
        if isinstance(other, Callable):
            if method := self.hasMethod("Call"):
                if method == other:
                    return True

        return False


def Is(a, b):
    match (a, b):
        case (TypedVariable, _):
            return a == b
        case (ClassType, _):
            return a.isInstance(b)
        case (Callable, _):
            return a == b

    return False
