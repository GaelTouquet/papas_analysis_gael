from ROOT import TFile, TH1F, TF1, TCanvas
from cpyroot.tools.histcomparator import HistComparator as HistComp
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator

fil = TFile('./rootfiles/neutral_hadron_test_tree2.root')
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


can2 = TCanvas()
tree.Draw("cmsjet_22_e/cmsjet_e:gen_jet_e>>m(200,0,70,200,0,1.2)","gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1","colz")
can2.SetLogz()

can3 = TCanvas()
tree.Draw("papasjet_22_e/papasjet_e:gen_jet_e>>h(200,0,70,200,0,1.2)","gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1","colz")
can3.SetLogz()


can2b = TCanvas()
tree.Draw("cmsjet_22_e/gen_jet_e:gen_jet_e>>h2(200,0,70,200,0,1.2)","gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1","colz")
can2b.SetLogz()

can3b = TCanvas()
tree.Draw("papasjet_22_e/gen_jet_e:gen_jet_e>>h3(200,0,70,200,0,1.2)","gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1","colz")
can3b.SetLogz()

can2c = TCanvas()
tree.Draw("cmsjet_130_e/gen_jet_e:gen_jet_e>>h4(200,0,70,200,0,2)","gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/gen_jet_e<0.01","colz")
can2c.SetLogz()

can3c = TCanvas()
tree.Draw("papasjet_130_e/gen_jet_e:gen_jet_e>>h5(200,0,70,200,0,2)","gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && papasjet_22_e/gen_jet_e<0.01","colz")
can3c.SetLogz()

can12 = TCanvas()
tree.Draw("cmsjet_e/gen_jet_e:gen_jet_e>>h6(200,0,70,200,0,2)","gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1","colz")
can12.SetLogz()

can12b = TCanvas()
tree.Draw("papasjet_e/gen_jet_e:gen_jet_e>>h7(200,0,70,200,0,2)","gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1","colz")
can12b.SetLogz()

can12c = TCanvas()
tree.Draw("papasjet_e/gen_jet_e:gen_jet_e>>h9(200,0,70,200,0,2)","gen_jet_pt>1 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.01","colz")
can12c.SetLogz()

