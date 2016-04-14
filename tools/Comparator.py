from ROOT import TLegend, TCanvas
from papas_analysis_gael.tools.style import cms_style, papas_style

class Comparator(object):
    
    def __init__(self, tree1, tree2, plotter, 
                 style1, style2, plotter_args = {}):
        self.plotter = plotter
        self.plotter_args = plotter_args
        self.style1 = style1
        self.style2 = style2
        self.tree1 = tree1
        self.tree2 = tree2
        self.plot()

    def Draw(self, same = False):
        self.plotter1.Draw(same = same)
        self.plotter2.Draw(same = True)
        if ':' not in self.plotter_args['var']:
            self.plotter1.hist.GetYaxis().SetRangeUser(1,
                                    self.ymax(self.plotter1.hist,
                                              self.plotter2.hist)*1.2)
        self.legend = TLegend(0.7, 0.8, 0.9, 0.9)
        self.legend.AddEntry(self.plotter1.hist, self.style1.label, 'lp')
        self.legend.AddEntry(self.plotter2.hist, self.style2.label, 'lpf')
        self.legend.SetFillColor(0)
        self.legend.Draw('same')

    def plot(self):
        self.plotter1 = self.plotter(self.tree1, self.plotter_args, self.style1)
        self.plotter2 = self.plotter(self.tree2, self.plotter_args, self.style2)

    def ymax(self, h1=None, h2=None):
        '''Returns the best y axis maximum so that h1 and h2 are both visible.'''
        def getmax(h):
            return  h.GetBinContent(h.GetMaximumBin())
        if h1 is None: h1 = self.h1
        if h2 is None: h2 = self.h2
        ymax = max(getmax(h1), getmax(h2))
        if ymax == 0:
            ymax = 1
        return ymax

class CompHandler(object):
    
    def __init__(self, tree1, tree2, plotter,
                 style1 = papas_style, style2 = cms_style, 
                 *args, **kwargs):
        self.canvas = []
        self.tree1, self.tree2 = tree1, tree2
        self.plotter = plotter
        self.style1, self.style2 = style1, style2
        self.plot_args = kwargs
        self.comp = Comparator(self.tree1, self.tree2, plotter,
                               style1, style2, self.plot_args)
        self.Draw()

    def change(self, draw = True, log = False, same = False, 
               style1 = None, style2 = None, *args, **kwargs):
        if not style1:
            style1 = self.style1
        if not style2:
            style2 = self.style2
        for key in kwargs.keys():
            if key == 'cutadd':
                self.plot_args['cut'] += ' && '+kwargs[key]
            else:
                self.plot_args[key] = kwargs[key]
        i = 1
        while hasattr(self, 'comp'+str(i)):
            i += 1
        setattr(self, 'comp'+str(i),
                Comparator(self.tree1, self.tree2, self.plotter,
                           style1, style2, self.plot_args))
        if draw:
            self.Draw(str(i), same=same)
        if draw and log:
            self.canvas[i].SetLogy()

    def Draw(self, i = '',same = False):
        if not same:
            self.canvas.append(TCanvas())
        getattr(self, 'comp'+str(i)).Draw(same=same)
