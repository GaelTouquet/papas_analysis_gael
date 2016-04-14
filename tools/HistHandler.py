from papas_analysis_gael.tools.Hist import Hist
from ROOT import TCanvas

class HistHandler(object):
    
    def __init__(self, tree, style, *args, **kwargs):
        self.canvas = []
        self.tree = tree
        self.style = style
        self.args = kwargs
        self.hists = []
        self.build()

    def build(self):
        self.hists.append(Hist(self.tree, self.args, self.style))

    def change(self, draw = True, log = False, *args, **kwargs):
        for key in kwargs.keys():
            if key == 'cutadd':
                self.args['cut'] += ' && '+kwargs[key]
            else:
                self.args[key] = kwargs[key]
        self.build()
        if draw:
            self.Draw()
            if log:
                self.canvas[-1].SetLogy()

    def Draw(self, same = False):
        if not same:
            self.canvas.append(TCanvas())
        self.hists[-1].Draw()
