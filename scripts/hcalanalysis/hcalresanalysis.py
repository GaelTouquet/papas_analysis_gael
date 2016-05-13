from ROOT import TFile, TH2F, TCanvas, TF1
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator
from cpyroot.tools.fitter2d import Fitter2D

fil = TFile('./rootfiles/neutral_hadron_tree.root')
tree = fil.Get('events')

comp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_pt>50 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.1',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_pt>50 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.1')

#comp2 = HistComparator(tree, style1 = cms_style, style2 = papas_style,
#                      nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}/E_{gen}',
#                      var1 = 'cmsjet_e/gen_jet_e', 
#                      cut1 = 'gen_jet_pt>50 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.1',
#                      var2 = 'papasjet_e/gen_jet_e',
#                       cut2 = 'gen_jet_pt>50 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.1')

fitterb = Fitter2D('histo2db','E_{rec}/E_{gen}vsE_{gen} barrel', 200, 5, 100, 200, 0, 2)
tree.Project('histo2db','cmsjet_e/gen_jet_e:gen_jet_e','gen_jet_pt>1 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01')
fitterb.fit_slices()
can3b = TCanvas()
fitterb.h2d.Draw()
canb = TCanvas()
fitterb.hmean.SetTitle('Fitted value of mean barrel')
fitterb.hmean.Draw()
response = TF1('response','[0]/(1+exp((x-[1])/[2]))')
response.SetParameter(0,1.)
response.SetParameter(1,3.)
response.SetParameter(2,-5.)
#response2 = TF1('response2','[0]*(1-exp(-(x-[1])/[2]))')
#response2.SetParameter(0,1.)
#response2.SetParameter(1,10.)
#response2.SetParameter(2,10.)
#response2.SetLineColor(1)
fitterb.hmean.Fit('response', 'B')
#fitterb.hmean.Fit('response2', 'B same')
can2b = TCanvas()
fitterb.hsigma.SetTitle('Fitted value of Sigma barrel')
fitterb.hsigma.Draw()
eres = TF1('eres','sqrt(([0]/sqrt(x))**2+([1]/x)**2+[2]**2)')
fitterb.hsigma.Fit('eres')

cantoto = TCanvas()
tree.Draw('cmsjet_e/gen_jet_e:gen_jet_e>>h7(200,0,70,200,0,2)','gen_jet_pt>1 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01','colz')
cantoto.SetLogz()
