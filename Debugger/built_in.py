import uuid


class NoPatternMatched:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __repr__(self):
        return f"NoPatternMatched({self.value})"

    def __str__(self):
        return f"NoPatternMatched({self.value})"

    def __hash__(self):
        return hash(self.id)


class UnknownType:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __repr__(self):
        return f"UnknownType({self.value})"

    def __str__(self):
        return f"UnknownType({self.value})"

    def __hash__(self):
        return hash(self.id)


class TypeNotMatched:
    def __init__(self, value=None):
        self.value = value
        self.id = uuid.uuid4()

    def __repr__(self):
        return f"TypeNotMatched({self.value})"

    def __str__(self):
        return f"TypeNotMatched({self.value})"

    def __hash__(self):
        return hash(self.id)
