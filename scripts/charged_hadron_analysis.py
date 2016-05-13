from ROOT import TFile
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator

fil = TFile('./rootfiles/charged_hadron_tree.root')
tree = fil.Get('events')

comp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 200, xmin = 0.5, xmax = 1.5, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.479 && simtrack_len==3',
                      var2 = 'papasjet_e/gen_jet_e')

comp2 = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 200, xmin = 0.5, xmax = 1.5, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)>1.479 && abs(gen_jet_eta)<3 && simtrack_len==3',
                      var2 = 'papasjet_e/gen_jet_e')
