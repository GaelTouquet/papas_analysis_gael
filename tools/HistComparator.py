from ROOT import TCanvas, TLegend, TH1F

class HistComparator(object):

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree
        self.args = kwargs
        self.canva = TCanvas()
        self.build()
        self.Draw(same = False)

    def build(self):
        self.nbin = self.args['nbin']
        self.xmin, self.xmax = self.args['xmin'], self.args['xmax']
        self.var1, self.var2 = self.args['var1'], self.args['var2']
        if 'cut' in self.args:
            self.cut1, self.cut2 = self.args['cut'], self.args['cut']
        else:
            self.cut1, self.cut2 = self.args['cut1'], self.args['cut2']
        self.style1, self.style2 = self.args['style1'], self.args['style2']
        if self.var1 == self.var2:
            self.title = '#splitline{'+self.var1+'}'
        else:
            self.title = '#splitline{'+self.var1+' & '+self.var2+'}'
        if self.cut1 == self.cut2:
            self.title += '{cut('+self.cut1+')}'
        else:
            self.title += '{cut('+self.cut1+' & '+self.cut2+')}'
        self. xvar = self.args['xvar']
        self.hist1 = TH1F('hist1', self.title, self.nbin, self.xmin, self.xmax)
        self.tree.Project('hist1', self.var1, self.cut1)
        self.hist1.GetXaxis().SetTitle(self.args['xvar'])
        self.hist1.SetStats(0)
        #self.hist1.GetXaxis().SetTitleOffset(0.9)
        self.hist1.Sumw2()
        self.style1.markerStyle = 1
        self.style1.formatHisto(self.hist1)
        self.hist2 = TH1F('hist2', 'title', self.nbin, self.xmin, self.xmax)
        self.tree.Project('hist2', self.var2, self.cut2)
        self.hist2.GetXaxis().SetTitle(self.args['xvar'])
        self.hist2.SetStats(0)
        #self.hist2.GetXaxis().SetTitleOffset(0.9)
        self.hist1.GetYaxis().SetTitle('N_{events}')
        self.hist2.Sumw2()
        self.style2.markerStyle = 1
        self.style2.formatHisto(self.hist2)

    def Draw(self, same = False):
        if same:
            self.hist1.Draw("same hist")
        else:
            self.hist1.Draw("hist")
        self.hist2.Draw("same hist")
        self.hist1.GetYaxis().SetRangeUser(1e-1,
                                        self.ymax(self.hist1, self.hist2)*1.2)
        self.legend = TLegend(0.7, 0.8, 0.9, 0.9)
        self.legend.AddEntry(self.hist1, self.style1.label, 'lp')
        self.legend.AddEntry(self.hist2, self.style2.label, 'lp')
        self.legend.SetFillColor(0)
        self.legend.Draw('same')

    def change(self, same = False, log = False, *args, **kwargs):
        for key in kwargs.keys():
            if key == 'cut':
                self.args['cut1'] = kwargs[key]
                self.args['cut2'] = kwargs[key]
            else:
                self.args[key] = kwargs[key]
        self.build()
        self.Draw(same = same)
        if log:
            self.canva.SetLogy()

    def add(self, *args, **kwargs):
        self.addargs = {}
        for key in self.args.keys():
            if key in kwargs:
                self.addargs[key] = kwargs[key]
            else:
                self.addargs[key] = self.args[key]
        i = 3
        while hasattr(self, 'hist'+str(i)):
            i += 1
        setattr(self, 'hist'+str(i), 
                TH1F('hist'+str(i), '', self.nbin, self.xmin, self.xmax))
        self.tree.Project('hist'+str(i), self.addargs['var1'], self.addargs['cut1'])
        self.addargs['style1'].formatHisto(getattr(self, 'hist'+str(i)))
        getattr(self, 'hist'+str(i)).Draw('same histo')
        ymax = max(self.ymax(self.hist1, self.hist2),
                   self.ymax(self.hist1, getattr(self, 'hist'+str(i))))
        self.hist1.GetYaxis().SetRangeUser(1e-1,
                                           ymax*1.2)
        self.legend.AddEntry(getattr(self, 'hist'+str(i)), self.addargs['style1'].label, 'lp')

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
