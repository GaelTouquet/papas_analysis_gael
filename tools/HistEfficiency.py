from ROOT import gDirectory, TH1F

class HistEfficiency(object):

    def __init__(self, tree, args, style):
        self.tree = tree
        self.nbin = args['nbin']
        self.xmin, self.xmax = args['xmin'], args['xmax']
        self.var = args['var']
        self.cut, self.eff_cut = args['cut'], args['eff_cut']
        self.style = style
        self.hists = {}
        self.create_hist('rec', self.var, 
                         ' && '.join([self.cut, self.eff_cut]))
        self.create_hist('gen', self.var, self.cut)
        self.create_hist('ratio', '', '')
        self.hist = gDirectory.Get('ratio')
        self.hist.Divide(self.hists['rec'], 
                          self.hists['gen'],
                          1,1,
                          'B')
        self.ratiosetup( args['varname'])
        
    def create_hist(self, title, var, cut):
        self.hists[title] = TH1F(title ,title, self.nbin, self.xmin, self.xmax)
        if title != 'ratio':
            self.tree.Project(title, var, cut)
            self.hists[title].Sumw2()

    def Draw(self, same = False):
        self.style.formatHisto(self.hist)
        if same:
            self.hist.Draw("SAME")
        else:
            self.hist.Draw()

    def ratiosetup(self, varname):
        title = '#splitline{efficiency : '+self.var+'}'
        title += '{cut('+self.cut+')'
        title += ' effcut('+self.eff_cut+')}'
        self.hist.SetTitle(title)
        self.hist.SetStats(0)
        self.hist.GetXaxis().SetTitle(varname)
        self.hist.GetXaxis().SetTitleOffset(0.9)
