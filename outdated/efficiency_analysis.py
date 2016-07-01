from ROOT import TFile, TLegend
from HistEfficiency import HistEfficiency
from style import papas_style, cms_style

papas_file = TFile('./rootfiles/papassampletuned2.root')
cms_file = TFile('./rootfiles/cmssamplejetted.root')
papas = papas_file.Get('events')
cms = cms_file.Get('events')

class comparator(object):
    
    def __init__(self, tree1, tname1, tree2, tname2,
                 var, cut, eff_cut,
                 xmin, xmax, title,
                 nbin = 100, style1 = papas_style, style2 = cms_style, 
                 varname = '',
                 efficiency_name = 'efficiency'):
        self.title, self.tname1, self.tname2 = title, tname1, tname2
        self.histeff1 = HistEfficiency(tree1, var, cut, eff_cut,  
                                       xmin, xmax, nbin, 
                                       style1, varname, 
                                       efficiency_name)
        self.histeff2 = HistEfficiency(tree2, var, cut, eff_cut,  
                                       xmin, xmax, nbin, 
                                       style2, varname, 
                                       efficiency_name)
        self.draw(True)

    def draw(self, same = False):
        if same:
            self.histeff1.ratio.SetTitle(' '.join([self.histeff1.ratio.GetTitle(),self.title]))
            self.histeff1.ratio.GetYaxis().SetRangeUser(0.,1.)
            self.histeff1.draw()
            self.histeff2.draw(same = True)
            self.legend = TLegend(0.35, 0.15, 0.65, 0.25)
            self.legend.AddEntry(self.histeff1.ratio,
                                 self.tname1, 'lp')
            self.legend.AddEntry(self.histeff2.ratio,
                                 self.tname2, 'lpf')
            self.legend.SetFillColor(0)
            self.legend.Draw('same')
        else:
            self.histeff1.draw()
            self.histeff2.draw()

pt_comp = comparator(papas, 'papas', cms, 'cms',
                     'jet1_pt',
                     'jet1_pt>1 && jet1_pt<10',
                     'jet1_rec_211_num==1',
                     0,10,'(1>P_{T}>10)', nbin = 100,style1 = papas_style, 
                     style2 = cms_style,
                     varname = 'P_{T} (GeV)',
                     efficiency_name ='tracking efficiency')

pt_comp2 = comparator(papas, 'papas', cms, 'cms',
                     'jet1_pt',
                     'jet1_pt>1 && jet1_pt<10 && abs(jet1_eta)<1.3',
                     'jet1_rec_211_num==1',
                     0,10,'(1>P_{T}>10 & eta<1.3)',
                      nbin = 100,style1 = papas_style, 
                     style2 = cms_style,
                     varname = 'P_{T} (GeV)',
                     efficiency_name ='tracking efficiency')

pt_comp3 = comparator(papas, 'papas', cms, 'cms',
                     'jet1_pt',
                     'jet1_pt>1 && jet1_pt<10 && abs(jet1_eta)<2.6 && abs(jet1_eta)>1.3',
                     'jet1_rec_211_num==1',
                     0,10,'(1>P_{T}>10 & 1.3<eta<2.6)',
                      nbin = 100,style1 = papas_style, 
                     style2 = cms_style,
                     varname = 'P_{T} (GeV)',
                     efficiency_name ='tracking efficiency')


eta_comp = comparator(papas, 'papas', cms, 'cms',
                     'jet1_eta',
                     'jet1_pt>1 && jet1_pt<10',
                     'jet1_rec_211_num==1',
                     -3,3,'(1>P_{T}>10)', nbin = 100,style1 = papas_style, 
                      style2 = cms_style,
                     varname = 'eta',
                     efficiency_name ='tracking efficiency')
