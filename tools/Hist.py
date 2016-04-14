from ROOT import TH1F, TH2F, TCanvas
import copy

class Hist(object):

    def __init__(self, tree, args, style):
        self.tree = tree
        self.args = args
        self.style = style
        self.build()

    def build(self):
        self.nbin = self.args['nbin']
        self.xmin, self.xmax = self.args['xmin'], self.args['xmax']
        self.var = self.args['var']
        self.cut = self.args['cut']
        self.title = '#splitline{'+self.var+'}'
        self.title += '{cut('+self.cut+')}'
        self.xvar = self.args['xvar'] if 'xvar' in self.args else self.var
        if ':' in self.var:
            self.ymin, self.ymax = self.args['ymin'], self.args['ymax']
            self.hist = TH2F('hist', self.title, 
                             self.nbin, self.xmin, self.xmax, 
                             self.nbin, self.ymin, self.ymax)
            self.yvar = self.args['yvar'] if 'yvar' in self.args else ''
            self.hist.GetYaxis().SetTitle(self.yvar)
        else:
            self.hist = TH1F('hist', self.title, 
                             self.nbin, self.xmin, self.xmax)
        self.hist.GetXaxis().SetTitle(self.args['xvar'])
        self.tree.Project('hist', self.var, self.cut)
        self.hist.SetStats(0)
        self.hist.GetXaxis().SetTitleOffset(0.9)
        self.hist.Sumw2()

    def Draw(self, same = False):
        self.style.markerStyle = 1
        self.style.formatHisto(self.hist)
        if ':' in self.var:
            if same:
                self.hist.Draw('same LEGO')
            else:
                self.hist.Draw('LEGO')
        else:
            if same:
                self.hist.Draw('same HIST E')
            else:
                self.hist.Draw('HIST E')

    def change(self, draw = True, log = False, *args, **kwargs):
        for key in kwargs.keys():
            if key == 'cutadd':
                self.args['cut'] += ' && '+kwargs[key]
            else:
                self.args[key] = kwargs[key]
        self.build()
        if draw:
            i = 1
            while hasattr(self, 'canva'+str(i)):
                i += 1
            setattr(self, 'canva'+str(i), TCanvas())
            self.Draw(str(i))
            if log:
                getattr(self, 'canva'+str(i)).SetLogy()
