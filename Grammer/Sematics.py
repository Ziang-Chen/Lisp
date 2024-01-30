import Grammer.Tokens as Tokens
import operator as op

defaultOperation = {
Tokens.Add : op.add,
Tokens.And : op.and_,
#Tokens.AnnAssign : 
#Tokens.Assert : 
#Tokens.Assign :
#Tokens.AsyncFor :
#Tokens.AsyncFunctionDef :
#Tokens.AsyncWith :
#Tokens.AsyncWithItem :
#Tokens.Attribute :
#Tokens.AugAssign :
Tokens.BitwiseAnd : op.and_,
Tokens.BitwiseNot : op.invert,
Tokens.BitwiseOr : op.or_,
Tokens.BitwiseXor : op.xor,
Tokens.Boolean : bool,
#Tokens.Break : 
#Tokens.Call :
#Tokens.ClassDef :
#Tokens.Continue :
#Tokens.Delete :
Tokens.Dict : dict,
Tokens.Divide : op.truediv,
#Tokens.Ellipsis : 
#Tokens.Equal :
#Tokens.ExceptHandler :
#Tokens.Exec :
Tokens.FloorDivide : op.floordiv,
#Tokens.For :
#Tokens.FunctionDef :
#Tokens.Global :
Tokens.GreaterThan : op.gt,
Tokens.GreaterThanEqual : op.ge,
#Tokens.If :
#Tokens.Import :
#Tokens.ImportFrom :
Tokens.In : op.contains,
#Tokens.Index : 
Tokens.Is : op.is_,
Tokens.IsNot : op.is_not,
#Tokens.Lambda : 
Tokens.LeftShift : op.lshift,
Tokens.LessThan : op.lt,
Tokens.LessThanEqual : op.le,
Tokens.List : list,
Tokens.Modulo : op.mod,
Tokens.Multiply : op.mul,
#Tokens.Name : 
#Tokens.NameConstant :
#Tokens.NoneType :
#Tokens.Nonlocal :
Tokens.Not : op.not_,
Tokens.NotEqual : op.ne,
#Tokens.NotIn : 
#Tokens.Number :
Tokens.Or : op.or_,
#Tokens.Pass :
#Tokens.Power :
Tokens.Print : print,
#Tokens.Raise :
#Tokens.Return :
#Tokens.RightShift :
Tokens.Set : set,
#Tokens.Slice :
Tokens.String : str,
Tokens.Subtract : op.sub,
#Tokens.Try :
Tokens.Tuple : tuple,
Tokens.UnaryAdd : op.pos,
Tokens.UnaryInvert : op.invert,
Tokens.UnarySubtract : op.neg,
#Tokens.Variable :
#Tokens.While :
#Tokens.With :
#Tokens.WithItem :
#Tokens.Yield :
#Tokens.YieldFrom :
}

