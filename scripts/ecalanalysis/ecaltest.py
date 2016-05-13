from ROOT import TFile
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator

fil = TFile('./rootfiles/photon_test.root')
tree = fil.Get('events')

comp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3')

comp2 = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3')

comp2.change(cut = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3 && simtrack_len>5')

errcomp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = -5, xmax = 5, xvar = 'E_{rec}-E_{gen}',
                      var1 = 'cmsjet_e-gen_jet_e', 
                      cut1 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3',
                      var2 = 'papasjet_e-gen_jet_e',
                      cut2 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3')

errcomp.add(style1 = cms_style2, var1 = 'cms_control_jet_e')
