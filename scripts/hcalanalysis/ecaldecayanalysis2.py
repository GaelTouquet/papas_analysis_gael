from ROOT import TFile
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator

fil = TFile('./rootfiles/neutral_hadron_test_tree2.root')
tree = fil.Get('events')

comp_22_e_barrel = HistComparator(tree, style1 = cms_style, 
                                  style2 = papas_style,
                      nbin = 200, xmin = 0, xmax = 5, xvar = 'E#gamma_{rec}',
                      var1 = 'cmsjet_22_e', 
                      cut = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1',
                      var2 = 'papasjet_22_e')

comp_22_e_barrel.hist1.GetYaxis().SetRangeUser(0, 1800)

comp_22_highe_barrel = HistComparator(tree, style1 = cms_style, 
                                  style2 = papas_style,
                      nbin = 200, xmin = 5, xmax = 100, xvar = 'E#gamma_{rec}',
                      var1 = 'cmsjet_22_e', 
                      cut = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1',
                      var2 = 'papasjet_22_e')

comp_22_erel_barrel = HistComparator(tree, style1 = cms_style, 
                                  style2 = papas_style,
                      nbin = 200, xmin = 0, xmax = 1.1, xvar = 'E#gamma_{rec}/E_{rec}',
                      var1 = 'cmsjet_22_e/gen_jet_e', 
                      cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1',# && cmsjet_22_e/cmsjet_e>0
                      var2 = 'papasjet_22_e/gen_jet_e',
                                     cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1')# && papasjet_22_e/papasjet_e>0

comp_22_erel_barrel2 = HistComparator(tree, style1 = cms_style, 
                                  style2 = papas_style,
                      nbin = 200, xmin = 0, xmax = 1.1, xvar = 'E#gamma_{rec}/E_{rec}',
                      var1 = 'cmsjet_22_e/cmsjet_e', 
                      cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3',# && cmsjet_22_e/cmsjet_e>0
                      var2 = 'papasjet_22_e/papasjet_e',
                                     cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3')# && papasjet_22_e/papasjet_e>0

#comp_22_erel_barrel.hist1.GetYaxis().SetRangeUser(0, 2500)

cms_int = comp_22_erel_barrel.hist1.Integral()
papas_int = comp_22_erel_barrel.hist2.Integral()
print 'cms :', cms_int, 'papas :', papas_int

