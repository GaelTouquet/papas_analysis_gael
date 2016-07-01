from ROOT import TFile
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator
import tdrstyle 

fil = TFile('./rootfiles/photon_tree.root')
tree = fil.Get('events')

e_rec_e_gen = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 300, xmin = 0.8, xmax = 1.2, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'cmsjet_e>20 && cmsjet_e<100 && abs(cmsjet_eta)<1.5 && simtrack_len==3',
                      var2 = 'papasjet_e/gen_jet_e',
                        cut2 = 'papasjet_e>20 && papasjet_e<100 && abs(papasjet_eta)<1.5 && simtrack_len==3')

comp_e_barrel = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = 0, xmax = 1, xvar = 'E_{rec} (GeV)',
                      var1 = 'cmsjet_e', 
                      cut1 = 'cmsjet_e>0 && cmsjet_e<1 && abs(cmsjet_eta)<1.4',
                      var2 = 'papasjet_e',
                        cut2 = 'papasjet_e>0 && papasjet_e<1 && abs(papasjet_eta)<1.4 && simtrack_len==3')

comp_e_endcap = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec} (GeV)',
                      var1 = 'cmsjet_e', 
                      cut1 = 'cmsjet_e>0 && cmsjet_e<3 && abs(cmsjet_eta)<3 && abs(cmsjet_eta)>1.5 && simtrack_len==3',
                      var2 = 'papasjet_e',
                        cut2 = 'papasjet_e>0 && papasjet_e<3 && abs(papasjet_eta)<3 && abs(papasjet_eta)>1.5 && simtrack_len==3')

# comp_e_endcap_gamma = HistComparator(tree, style1 = cms_style, style2 = papas_style,
#                       nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}',
#                       var1 = 'cmsjet_22_e', 
#                       cut1 = 'cmsjet_e>0 && cmsjet_e<3 && abs(cmsjet_eta)<3 && abs(cmsjet_eta)>1.5 && simtrack_len==3',
#                       var2 = 'papasjet_22_e',
#                         cut2 = 'papasjet_e>0 && papasjet_e<3 && abs(papasjet_eta)<3 && abs(papasjet_eta)>1.5 && simtrack_len==3')

# comp_e_endcap_elec = HistComparator(tree, style1 = cms_style, style2 = papas_style,
#                       nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}',
#                       var1 = 'cmsjet_11_e', 
#                       cut1 = 'cmsjet_e>0 && cmsjet_e<3 && abs(cmsjet_eta)<3 && abs(cmsjet_eta)>1.5 && simtrack_len==3',
#                       var2 = 'papasjet_11_e',
#                         cut2 = 'papasjet_e>0 && papasjet_e<3 && abs(papasjet_eta)<3 && abs(papasjet_eta)>1.5 && simtrack_len==3')

# comp_e_endcap_hadron = HistComparator(tree, style1 = cms_style, style2 = papas_style,
#                       nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}',
#                       var1 = 'cmsjet_130_e', 
#                       cut1 = 'cmsjet_e>0 && cmsjet_e<3 && abs(cmsjet_eta)<3 && abs(cmsjet_eta)>1.5 && simtrack_len==3',
#                       var2 = 'papasjet_130_e',
#                         cut2 = 'papasjet_e>0 && papasjet_e<3 && abs(papasjet_eta)<3 && abs(papasjet_eta)>1.5 && simtrack_len==3')

# comp_e_endcap_hadron_control = HistComparator(tree, style1 = cms_style, style2 = papas_style,
#                       nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}',
#                       var1 = 'cms_control_jet_130_e', 
#                       cut1 = 'cmsjet_e>0 && cmsjet_e<3 && abs(cmsjet_eta)<3 && abs(cmsjet_eta)>1.5 && simtrack_len==3',
#                       var2 = 'papas_control_jet_130_e',
#                         cut2 = 'papasjet_e>0 && papasjet_e<3 && abs(papasjet_eta)<3 && abs(papasjet_eta)>1.5 && simtrack_len==3')

# comp_eta_endcap = HistComparator(tree, style1 = cms_style, style2 = papas_style,
#                       nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}',
#                       var1 = 'cmsjet_eta', 
#                       cut1 = 'cmsjet_e>0 && cmsjet_e<3 && abs(cmsjet_eta)<3 && abs(cmsjet_eta)>1.5 && simtrack_len==3',
#                       var2 = 'papasjet_eta',
#                         cut2 = 'papasjet_e>0 && papasjet_e<3 && abs(papasjet_eta)<3 && abs(papasjet_eta)>1.5 && simtrack_len==3')

comp_pt_endcap = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = 0, xmax = 1, xvar = 'P_{Trec} (GeV)',
                      var1 = 'cmsjet_pt', 
                      cut1 = 'cmsjet_pt>0.2 && cmsjet_pt<1 && abs(cmsjet_eta)>1.5 && abs(cmsjet_eta)<3 && simtrack_len==3',
                      var2 = 'papasjet_pt',
                         cut2 = 'papasjet_e>0 && papasjet_pt<1 && abs(papasjet_eta)>1.5 && abs(papasjet_eta)<3 && simtrack_len==3')
