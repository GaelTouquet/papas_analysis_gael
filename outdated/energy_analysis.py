from ROOT import TFile, TLegend, TH1F, TCanvas
from style import papas_style, cms_style

papas_file = TFile('./rootfiles/papassampletuned2.root')
cms_file = TFile('./rootfiles/cmssamplejetted.root')
papas_tree = papas_file.Get('events')
cms_tree = cms_file.Get('events')

class EReconstuctionComparator(object):
    
    def __init__(self, tree1, style1, tree2, style2):
        self.canva = TCanvas()
        name1 = 'rec/gen' + style1.label
        self.h1 = TH1F('h1','E_{rec}/E_{gen}', 100, 0, 3)
        tree1.Project('h1','jet1_rec_e/jet1_e','jet1_pt>1 && jet1_pt<10 && jet1_rec_pt>0')
        self.h1.Sumw2()
        self.h1.SetStats(0)
        style1.formatHisto(self.h1)
        self.h1.Draw()
        name2 = 'rec/gen' + style2.label
        self.h2 = TH1F('h2','E_{rec}/E_{gen}', 100, 0, 3)
        tree2.Project('h2','jet1_rec_e/jet1_e','jet1_pt>1 && jet1_pt<10 && jet1_rec_pt>0')
        self.h2.Sumw2()
        style2.formatHisto(self.h2)
        self.h2.Draw('same')
        self.legend = TLegend(0.6, 0.7, 0.9, 0.9)
        self.legend.AddEntry(self.h1, style1.label, 'lp')
        self.legend.AddEntry(self.h2, style2.label, 'lpf')
        self.legend.SetFillColor(0)
        self.legend.Draw('same')
        self.canva.SetLogy()

a = EReconstuctionComparator(papas_tree, papas_style, cms_tree, cms_style)
