import typing


class Var:
    def __init__(self, name: str, value=None) -> None:
        self.name = name
        self.value = value

    # def __eq__(self, other) -> bool:
    #    return self.name == other.name

    def __repr__(self) -> str:
        return f"Variable object: Var({self.name}): {self.value}"

    # def __str__(self) -> str:
    #    return self.name

    def __hash__(self) -> int:
        return hash(self.name)


class TypeVar:
    def __init__(self, n: str, t: str, value=None) -> None:
        self.name = n
        self.type = t
        self.value = value

    def __repr__(self) -> str:
        return f"TypeVar object: TypeVar({self.name}, {self.type}):{self.value}"

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other) -> bool:
        return self.type == other.type


class TypeName:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"TypeName object: TypeName({self.name})"

    def __hash__(self) -> int:
        return hash(self.name)
