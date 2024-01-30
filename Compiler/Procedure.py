from Compiler.ContextManager import ContextManager as CM
import Grammer.Tokens as Tokens


class Procedure:
    def __init__(self, name, args, body):
        self.name = name
        self.args = args
        self.body = body

    def call(self, args, env: CM, parser):
        if len(args) != len(self.args):
            raise Exception("Invalid number of arguments")

        env.enter()

        result = parser((Tokens.Add, 1, 1), env, parser)
        for i, arg in enumerate(args):
            #    # env[self.args[i]] = arg
            result = parser((Tokens.Assign, self.args[i], arg), result.context, parser)

            # if isinstance(sa, tuple):
            #    result = parser((Tokens.Assign, sa[0], a), env, parser)
            #    env[sa[1]] = result
            # else:
            #    env[sa] = a
            # result = parser((Tokens.Assign, sa, a), env, parser)

        for expr in self.body:
            if expr[0] == Tokens.Return:
                result = parser(expr, result.context, parser)
                break
            result = parser(expr, result.context, parser)

        env.leave()
        return result

    def callWithoutArgs(self, env, parser):
        env.enter()
        result = parser((Tokens.Add, 1, 1), env, parser)
        for expr in self.body:
            if expr[0] == Tokens.Return:
                result = parser(expr, result.context, parser)
                break
            result = parser(expr, result.context, parser)

        env.leave()
        return result

    def __str__(self):
        return "Standard Procedure: \n" f"{self.name}" f"{self.args} \n" f"{self.body}"
