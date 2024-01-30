import unittest

# from Compiler.Context import Context
# from Compiler.ContextManager import ContextManager
# from Compiler.Symbol import Var


class Test_Context(unittest.TestCase):
    def test_context(self):
        from Compiler.Context import Context

        context = Context(None)
        context["a"] = 1
        context["b"] = 2
        context["c"] = 3
        context["d"] = 4
        self.assertEqual(context["a"], 1)
        self.assertEqual(context["b"], 2)
        self.assertEqual(context["c"], 3)
        self.assertEqual(context["d"], 4)
        # self.assertEqual(context.a, 1)
        # self.assertEqual(context.b, 2)
        # self.assertEqual(context.c, 3)
        # self.assertEqual(context.d, 4)
        # context.a = 5
        # context.b = 6
        # context.c = 7
        # context.d = 8
        # self.assertEqual(context["a"], 5)
        # self.assertEqual(context["b"], 6)
        # self.assertEqual(context["c"], 7)
        # self.assertEqual(context["d"], 8)
        # self.assertEqual(context.a, 5)
        # self.assertEqual(context.b, 6)
        # self.assertEqual(context.c, 7)
        # self.assertEqual(context.d, 8)
        del context["a"]
        del context["b"]
        del context["c"]
        del context["d"]
        self.assertEqual(context.names, [])
        self.assertEqual(context.content, {})
        # context.a = 1
        # context.b = 2
        # context.c = 3
        # context.d = 4
        # self.assertEqual(context.names, ["a", "b", "c", "d"])
        # self.assertEqual(context.content, {"a": 1, "b": 2, "c": 3, "d": 4})

        contextB = Context(dict())
        contextB["a"] = 8
        contextB["b"] = 7
        contextB["c"] = 6
        contextB["d"] = 5
        context["a"] = 1
        context["b"] = 2
        context["c"] = 3
        context["d"] = 4
        self.assertEqual(contextB["a"], 8)
        contextC = context + contextB
        self.assertEqual(contextC["a"], 8)
        self.assertEqual(contextC["b"], 7)
        self.assertEqual(contextC["c"], 6)
        self.assertEqual(contextC["d"], 5)
        # self.assertEqual(contextC.a, 8)
        # self.assertEqual(contextC.b, 7)
        # self.assertEqual(contextC.c, 6)
        # self.assertEqual(contextC.d, 5)

    def test_ContextWithVar(self):
        from Compiler.Context import Context
        from Compiler.Symbol import Var

        a = Var("a")
        b = Var("b")
        c = Var("c")
        d = Var("d")
        context = Context(None)
        context[a] = 1
        context[b] = 2
        context[c] = 3
        context[d] = 4
        self.assertEqual(context[a], 1)
        self.assertEqual(context[b], 2)
        self.assertEqual(context[c], 3)
        self.assertEqual(context[d], 4)


class Test_ContextManager(unittest.TestCase):
    def test_contextManager(self):
        from Compiler.Context import Context
        from Compiler.Symbol import Var
        from Compiler.ContextManager import ContextManager

        a = Var("a")
        b = Var("b")
        c = Var("c")
        d = Var("d")
        context = Context(
            {
                a: 1,
                b: 2,
                c: 3,
                d: 4,
            }
        )
        contextManager = ContextManager(context)
        self.assertEqual(contextManager[a], 1)
        self.assertEqual(contextManager[b], 2)
        self.assertEqual(contextManager[c], 3)
        self.assertEqual(contextManager[d], 4)

        contextManager.enter()
        contextManager[a] = 5
        contextManager[b] = 6
        contextManager[c] = 7
        contextManager[d] = 8
        self.assertEqual(contextManager[a], 5)
        self.assertEqual(contextManager[b], 6)
        self.assertEqual(contextManager[c], 7)
        self.assertEqual(contextManager[d], 8)

        contextManager.leave()
        self.assertEqual(contextManager[a], 1)
        self.assertEqual(contextManager[b], 2)
        self.assertEqual(contextManager[c], 3)
        self.assertEqual(contextManager[d], 4)

        contextManager.enter()
        contextManager.setGlobal(a, 9)
        contextManager.setGlobal(b, 10)
        contextManager.setGlobal(c, 11)
        contextManager.setGlobal(d, 12)
        contextManager.leave()
        self.assertEqual(contextManager[a], 9)
        self.assertEqual(contextManager[b], 10)
        self.assertEqual(contextManager[c], 11)
        self.assertEqual(contextManager[d], 12)

        contextManager.enter()
        contextManager[a] = 13
        contextManager.setGlobal(b, 14)
        contextManager.leave()
        self.assertEqual(contextManager[a], 9)
        self.assertEqual(contextManager[b], 14)

        contextManager.enter()
        contextManager.delGlobal(a)
        contextManager.leave()
        self.assertEqual(a in contextManager, False)
