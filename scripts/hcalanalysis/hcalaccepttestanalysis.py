from ROOT import TFile, TH1F, TF1, TCanvas
from cpyroot.tools.histcomparator import HistComparator as HistComp
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator

fil = TFile('./rootfiles/neutral_hadron_test_tree.root')
tree = fil.Get('events')

comp_e_barrel = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 200, xmin = 0, xmax = 20, xvar = 'E_{rec}',
                      var1 = 'cmsjet_e', 
                      cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.1',
                      var2 = 'papasjet_e',
                        cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.1')

comp_pt_barrel = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 200, xmin = 0, xmax = 20, xvar = 'Pt_{rec}',
                      var1 = 'cmsjet_pt', 
                      cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.1',
                      var2 = 'papasjet_pt',
                        cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.1')


e_cms = TH1F('e_cms','CMS energy',200, 0, 50)
tree.Project('e_cms','cmsjet_e', 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.1')
e_cms.Sumw2()
e_papas = TH1F('e_papas', 'Papas energy', 200, 0, 50)
tree.Project('e_papas','papasjet_e', 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.1')
e_papas.Sumw2()

e_comp = HistComp('efficiency factor', e_cms, e_papas)
e_comp.draw()
e_comp.ratio.Sumw2()
#lin = TF1('lin', '[0]*x+[1]')
#lin.SetRange(5., 15.)
#e_comp.ratio.Fit('lin', 'B R')
test = TF1('test', '1/(1+exp((x-[0])/[1]))')
test.SetParameter(0, 7.)
test.SetParameter(1, -2.)
test.SetRange(3., 50.)
e_comp.ratio.Fit('test', 'B R')

comp_e_endcap = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 200, xmin = 0, xmax = 20, xvar = 'E_{rec}',
                      var1 = 'cmsjet_e', 
                      cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.1',
                      var2 = 'papasjet_e',
                        cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.1')

comp_pt_endcap = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 200, xmin = 0, xmax = 20, xvar = 'Pt_{rec}',
                      var1 = 'cmsjet_pt', 
                      cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.1',
                      var2 = 'papasjet_pt',
                        cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.1')

e_cms_endcap = TH1F('e_cms_endcap','CMS energy',200, 0, 100)
tree.Project('e_cms_endcap','cmsjet_e', 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3  && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.1')
e_cms_endcap.Sumw2()
e_papas_endcap = TH1F('e_papas_endcap', 'Papas energy', 200, 0, 100)
tree.Project('e_papas_endcap','papasjet_e', 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3  && simtrack_len==1 && papasjet_22_e/papasjet_e<0.1')
e_papas_endcap.Sumw2()

e_comp_endcap = HistComp('efficiency factor endcap', e_cms_endcap, e_papas_endcap)
e_comp_endcap.draw()
e_comp_endcap.ratio.Sumw2()
e_comp_endcap.ratio.GetYaxis().SetRangeUser(0.2,1.2)
#lin = TF1('lin', '[0]*x+[1]')
#lin.SetRange(5., 15.)
#e_comp.ratio.Fit('lin', 'B R')
test2 = TF1('test2', '[2]/(1+exp((x-[0])/[1]))')
test2.SetParameter(0, 7.)
test2.SetParameter(1, -2.)
test2.SetRange(10., 100.)
e_comp_endcap.ratio.Fit('test2', 'B R')
test2.Draw('same')
test3 =  TF1('test3', '[0]+[1]*x+[2]*(x**2)')
test3.SetRange(3., 10.)
e_comp_endcap.ratio.Fit('test3', 'R')
test3.SetRange(1.1,10.)
test3.Draw('same')
