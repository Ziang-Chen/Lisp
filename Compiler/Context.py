import typing


class Context:
    def __init__(self, content=None):  # any type of key-value mapping
        # Context is a wrapper for a Mapping object
        # Always maintain a list of Names and contents
        # Name can be Var object
        if content is None:
            self.content = dict()
            self.names = []
        else:
            self.content = content
            self.names = list(content.keys())

    def __getitem__(self, name) -> typing.Any:
        # return based on self content
        if name in self.names:
            return self.content[name]
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )

    # def __getattr__(self, name) -> typing.Any:
    #     # return based on self content
    #     if name in ["BUILT_IN_names", "BUILT_IN_content"]:
    #         raise AttributeError(
    #             f"'{self.__class__.__name__}' Try to access Built-in parameter '{name}'"
    #         )
    #     else:
    #         raise AttributeError(
    #             f"'{self.__class__.__name__}' object has no attribute '{name}'"
    #         )

    def __setitem__(self, name, value) -> typing.Any:
        self.content[name] = value
        if name not in self.names:
            self.names.append(name)
        return value

    # def __setattr__(self, name, value) -> typing.Any:
    #     if name in ["BUILT_IN_names", "BUILT_IN_content"]:
    #         raise AttributeError(
    #             f"'{self.__class__.__name__}' Try to access Built-in parameter '{name}'"
    #         )

    #     self.BUILT_IN_content[name] = value
    #     if name not in self.BUILT_IN_names:
    #         self.BUILT_IN_names.append(name)
    #     return value

    def __delitem__(self, name):
        if name in self.names:
            del self.content[name]
            self.names.remove(name)
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )

    # def __delattr__(self, name):
    #     # del based on self content
    #     if name in ["BUILT_IN_names", "BUILT_IN_content"]:
    #         raise AttributeError(
    #             f"'{self.__class__.__name__}' Try to access Built-in parameter '{name}'"
    #         )

    #     if name in self.BUILT_IN_names:
    #         del self.BUILT_IN_content[name]
    #         self.BUILT_IN_names.remove(name)
    #     else:
    #         raise AttributeError(
    #             f"'{self.__class__.__name__}' object has no attribute '{name}'"
    #         )

    def __contains__(self, name) -> bool:
        return name in self.names

    def __iter__(self) -> typing.Iterator:
        return iter(self.names)

    def __len__(self) -> int:
        return len(self.names)

    def __repr__(self) -> str:
        return repr(self.content)

    def __str__(self) -> str:
        return str(self.content)

    def __bool__(self) -> bool:
        return bool(self.content)

    def __dir__(self) -> typing.List[str]:
        return self.names

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.content == other.content

    def __add__(self, other) -> typing.Any:
        # dict union
        # last seen wins
        return Context(self.content | other.content)

        # def __ne__(self, other) -> bool:

    #     return self.content != other.content

    # def __lt__(self, other) -> bool:
    #     return self.content < other.content

    # def __le__(self, other) -> bool:
    #     return self.content <= other.content

    # def __gt__(self, other) -> bool:
    #     return self.content > other.content

    # def __ge__(self, other) -> bool:
    #     return self.content >= other.content

    # def __sub__(self, other) -> typing.Any:
    #     return self.content - other.content

    # def __mul__(self, other) -> typing.Any:
    #     return self.content * other.content

    # def __matmul__(self, other) -> typing.Any:
    #     return self.content @ other.content

    # def __truediv__(self, other) -> typing.Any:
    #     return self.content / other.content

    # def __floordiv__(self, other) -> typing.Any:
    #     return self.content // other.content

    # def __mod__(self, other) -> typing.Any:
    #     return self.content % other.content

    # def __pow__(self, other) -> typing.Any:
    #     return self.content ** other.content

    # def __lshift__(self, other) -> typing.Any:
    #     return self.content << other.content

    # def __rshift__(self, other) -> typing.Any:
    #     return self.content >> other.content

    # def __and__(self, other) -> typing.Any:
    #     return self.content & other.content

    # def __xor__(self, other) -> typing.Any:
    #     return self.content ^ other.content

    # def __or__(self, other) -> typing.Any:
    #     return self.content | other.content

    # def __radd__(self, other) -> typing.Any:
    #     return other.content + self.content

    # def __rsub__(self, other) -> typing.Any:
    #     return other.content - self.content

    # def __rmul__(self, other) -> typing.Any:
    #     return other.content * self.content

    # def __rmatmul__(self, other) -> typing.Any:
    #     return other.content @ self.content

    # def __rtruediv__(self, other) -> typing.Any:
    #     return other.content / self.content

    # def __rfloordiv__(self, other) -> typing.Any:
    #     return other.content // self.content

    # def __rmod__(self, other) -> typing.Any:
    #     return other.content % self.content

    # def __rpow__(self, other) -> typing.Any:
    #     return other.content ** self.content

    # def __rlshift__(self, other) -> typing.Any:
    #     return other.content << self.content

    # def __rrshift__(self, other) -> typing.Any:
    #     return other.content >> self.content

    # def __rand__(self, other) -> typing.Any:
    #     return other.content & self.content

    # def __rxor__(self, other) -> typing.Any:
    #     return other.content ^ self.content

    # def __ror__(self, other) -> typing.Any:
    #     return other.content | self.content

    # def __iadd__(self, other) -> typing.Any:
    #     self.content += other.content
    #     return self.content

    # def __isub__(self, other) -> typing.Any:
    #     self.content -= other.content
    #     return self.content

    # def __imul__(self, other) -> typing.Any:
    #     self.content *= other.content
    #     return self.content

    # def __imatmul__(self, other) -> typing.Any:
    #     self.content @= other.content
    #     return self.content

    # def __itruediv__(self, other) -> typing.Any:
    #     self.content /= other.content
    #     return self.content

    # def __ifloordiv__(self, other) -> typing.Any:
    #     self.content //= other.content
    #     return self.content

    # def __imod__(self, other) -> typing.Any:
    #     self.content %= other.content
    #     return self.content

    # def __ipow__(self, other) -> typing.Any:
    #     self.content **= other.content
    #     return self.content

    # def __ilshift__(self, other) -> typing.Any:
    #     self.content <<= other.content
    #     return self.content

    # def __irshift__(self, other) -> typing.Any:
    #     self.content >>= other.content
    #     return self.content

    # def __iand__(self, other) -> typing.Any:
    #     self.content &= other.content
    #     return self.content

    # def __ixor__(self, other) -> typing.Any:
    #     self.content ^= other.content
    #     return self.content

    # def __ior__(self, other) -> typing.Any:
    #     self.content |= other.content
    #     return self.content

    # def __neg__(self) -> typing.Any:
    #     return -self.content

    # def __pos__(self) -> typing.Any:
    #     return +self.content

    # def __abs__(self) -> typing.Any:
    #     return abs(self.content)

    # def __invert__(self) -> typing.Any:
    #     return ~self.content

    # def __complex__(self) -> typing.Any:
    #     return complex(self.content)

    # def __int__(self) -> typing.Any:
    #     return int(self.content)

    # def __float__(self) -> typing.Any:
    #     return float(self.content)

    # def __round__(self, n=None) -> typing.Any:
    #     return round(self.content, n)

    # def __index__(self) -> typing.Any:
    #     return self.content.__index__()

    # def __enter__(self) -> typing.Any:
    #     return self.content.__enter__()

    # def __exit__(self, exc_type, exc_value, traceback) -> typing.Any:
    #     return self.content.__exit__(exc_type, exc_value, traceback)

    # def __await__(self) -> typing.Any:
    #     return self.content.__await__()

    # def __aiter__(self) -> typing.Any:
    #     return self.content.__aiter__()

    # def __anext__(self) -> typing.Any:
    #     return self.content.__anext__()

    # def __aenter__(self) -> typing.Any:
    #     return self.content.__aenter__()

    # def __aexit__(self, exc_type, exc_value, traceback) -> typing.Any:
    #     return self.content.__aexit__(exc_type, exc_value, traceback)

    # def __await__(self) -> typing.Any:
    #     return self.content.__await__()

    # def __aiter__(self) -> typing.Any:
    #     return self.content.__aiter__()

    # def __anext__(self) -> typing.Any:
    #     return self.content.__anext__()
