from ROOT import TFile
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator

fil = TFile('./rootfiles/neutral_hadron_test_tree.root')
tree = fil.Get('events')

relcomp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3 && cmsjet_e>0',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3 && papasjet_e>0')


abscomp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = -20, xmax = 20, xvar = 'E_{rec}-E_{gen}',
                      var1 = 'cmsjet_e-gen_jet_e', 
                      cut1 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3',
                      var2 = 'papasjet_e-gen_jet_e',
                      cut2 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3')
