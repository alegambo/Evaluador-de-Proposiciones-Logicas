__author__ = 'jszheng'
__coauthor__ = 'loriacarlos@gmail.com'

from wang.parser.grammar.WangVisitor import WangVisitor
from wang.parser.grammar.WangParser import WangParser

"""
    Tests Wang Visitor
    See grammar/Wang.g4
    based on jszheng git https://github.com/jszheng/py3antlr4book
    Example calc
"""
class WangPrintVisitor(WangVisitor):
    def __init__(self):
        pass
    def visitPremises(self, ctx):
        list_res=self.visit(ctx.sequence())
        return all(list_res)
    def visitAssertion(self,ctx):
        f=self.visit(ctx.formula(0))
        return f		
    def visitConclusions(self, ctx):
         list_res=self.visit(ctx.sequence())
         return any(list_res)              
    def visitFormExpr(self, ctx):
        # print(f'\nStart Visiting FormExpr (=>) {len(ctx.sequence())} children')
        res_premises = self.visit(ctx.premises())
        res_conclusions= self.visit(ctx.conclusions())
        return not res_premises or res_conclusions		
    
    def visitSeqExpr(self, ctx):
        print(f'Visiting SeqExpr (,) with {len(ctx.expr())} children')
        children = ctx.expr()
        return [self.visit(ch) for ch in children]
    
    def visitId(self, ctx):
        name = ctx.ID().getText()
        print(f'Visiting Id={name}')
        if name=="true": return True
        else: return False		
    def visitAndExpr(self, ctx):
        print('Visiting AndExpr (&)')
        res_left=self.visit(ctx.expr(0))
        res_right=self.visit(ctx.expr(1))
        return res_left and res_right

    def visitOrExpr(self, ctx):
        print('Visiting OrExpr (|)')
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        res_left=self.visit(ctx.expr(0))
        res_right=self.visit(ctx.expr(1))
        return res_left or res_right
       

    def visitParens(self, ctx):
        print('Visiting ParenExpr (...)')
        return self.visit(ctx.expr())

    def visitNotExpr(self, ctx):
        print('Visiting NotExpr (~) ')
        return not self.visit(ctx.expr())
        

    
