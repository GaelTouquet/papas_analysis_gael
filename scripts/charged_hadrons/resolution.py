from ROOT import TFile
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator

file = TFile('./rootfiles/charged_hadron_tree.root')
tree = file.Get('events')

Erec_Egen = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                           nbin = 500, xmin = 0., xmax = 3., 
                           xvar = 'E_{rec}/E_{gen}',
                           var1 = 'cmsjet_e/gen_jet_e',
                           cut = 'gen_jet_pt>1 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && gen_jet_e<100',
                           var2 = 'papasjet_e/gen_jet_e')
Erec_Egen.canva.SetLogy()

Echargedh_Egen = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                           nbin = 500, xmin = 0., xmax = 3., 
                           xvar = 'E_{h^{+}rec}/E_{gen}',
                           var1 = 'cmsjet_211_e/gen_jet_e',
                           cut = 'gen_jet_pt>1 && simtrack_len==1 && abs(gen_jet_eta)<1.3',
                           var2 = 'papasjet_211_e/gen_jet_e')
Echargedh_Egen.canva.SetLogy()

Ephoton_Egen = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                           nbin = 500, xmin = 0., xmax = 3., 
                           xvar = 'E_{#gamma rec}/E_{gen}',
                           var1 = 'cmsjet_22_e/gen_jet_e',
                           cut = 'gen_jet_pt>1 && simtrack_len==1 && abs(gen_jet_eta)<1.3',
                           var2 = 'papasjet_22_e/gen_jet_e')
Ephoton_Egen.canva.SetLogy()

Eneuth_Egen = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                           nbin = 500, xmin = 0., xmax = 3., 
                           xvar = 'E_{#gamma rec}/E_{gen}',
                           var1 = 'cmsjet_130_e/gen_jet_e',
                           cut = 'gen_jet_pt>1 && simtrack_len==1 && abs(gen_jet_eta)<1.3',
                           var2 = 'papasjet_130_e/gen_jet_e')
Eneuth_Egen.canva.SetLogy()

Erec_Egen_nochH = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                           nbin = 500, xmin = 0., xmax = 3., 
                           xvar = 'E_{rec}/E_{gen}',
                           var1 = 'cmsjet_e/gen_jet_e',
                           cut1 = 'gen_jet_pt>1 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && cmsjet_211_num==0',
                           var2 = 'papasjet_e/gen_jet_e',
                                 cut2 = 'gen_jet_pt>1 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && papasjet_211_num==0')
Erec_Egen_nochH.canva.SetLogy()

