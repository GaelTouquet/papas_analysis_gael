from ROOT import TFile, TH1F, TF1
from cpyroot.tools.histcomparator import HistComparator as HistComp
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator

fil = TFile('./rootfiles/neutral_hadron_test_tree2.root')
tree = fil.Get('events')

comp_e_barrel = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 300, xmin = 0, xmax = 30, xvar = 'E_{rec}',
                      var1 = 'cmsjet_e', 
                      cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.1',
                      var2 = 'papasjet_e',
                        cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.1')


e_cms = TH1F('e_cms','CMS energy',200, 0, 50)
tree.Project('e_cms','cmsjet_e', 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.1')
e_cms.Sumw2()
e_papas = TH1F('e_papas', 'Papas energy', 200, 0, 50)
tree.Project('e_papas','papasjet_e', 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.1')
e_papas.Sumw2()

e_comp = HistComp('efficiency factor', e_cms, e_papas)
e_comp.draw()
e_comp.ratio.GetYaxis().SetRangeUser(0.,1.5)
