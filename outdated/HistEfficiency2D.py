from ROOT import TCanvas, TH2F
from HistEfficiency import HistEfficiency
from cpyroot.tools.style import *

class HistEfficiency2D(HistEfficiency):
#TODO : varname
    def __init__(self, tree, var, cut, eff_cut,  xmin, xmax,
                 ymin, ymax, nbin = 100,
                 style = sBlack, varnamex = '',varnamey = '',
                 efficiency_name = 'efficiency',
                 label = ''):
        self.ymin, self.ymax = ymin, ymax
        self.varnamey = varnamey
        super(HistEfficiency2D, self).__init__(tree, var, cut, eff_cut,  
                                               xmin, xmax, nbin, 
                                               style, varnamex,
                                               efficiency_name,
                                               label)

    def create_hist(self, title, var, cut):
        self.hists[title] = TH2F(title ,title, 
                                 self.nbin, self.xmin, self.xmax,
                                 self.nbin, self.ymin, self.ymax)
        if title != 'ratio':
            self.tree.Project(title, var, cut)
            self.hists[title].Sumw2()

    def ratiosetup(self, label, var, varname, efficiency_name):
        self.ratio.SetTitle(label+'efficiency vs '+var)
        self.ratio.SetStats(0)
        self.ratio.GetXaxis().SetTitle(varname)
        self.ratio.GetYaxis().SetTitle(self.varnamey)

    def draw(self):
        self.canvas1 = TCanvas()
        self.style.formatHisto(self.ratio)
        self.ratio.Draw()
        self.canvas2 = TCanvas()
        self.ratio.Draw('LEGO')
