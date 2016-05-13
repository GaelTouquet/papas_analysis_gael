from ROOT import TFile, TH1F
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator

fil = TFile('./rootfiles/photon_test_tree.root')
tree = fil.Get('events')


fil2 = TFile('./rootfiles/photon_test.root')
tree2 = fil.Get('events')

histo1 = TH1F('histo1', 'histo1', 100, 0, 3)
tree.Project('histo1', 'control_cms_jet_e', 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3')
histo1.Sumw2()
histo1.Draw()

histo2 = TH1F('histo2', 'histo1', 100, 0, 3)
tree2.Project('histo2', 'control_cms_jet_e', 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3')
histo2.Sumw2()

ratio = TH1F('ratio', 'ratio of cones', 100, 0, 3)

ratio.Divide(histo1,histo2,1,1,'B')
ratio.Draw('hist e')
