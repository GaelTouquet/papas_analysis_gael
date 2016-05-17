from ROOT import TFile, TH2F, TCanvas, TF1
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator
from cpyroot.tools.fitter2d import Fitter2D

fil = TFile('./rootfiles/neutral_hadron_tree.root')
tree = fil.Get('events')

comp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 200, xmin = 0, xmax = 5, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.01')

fitterb = Fitter2D('histo2db','E_{rec}/E_{gen}vsE_{gen} barrel', 200, 0, 100, 200, 0, 2)
tree.Project('histo2db','cmsjet_e/gen_jet_e:gen_jet_e','gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01')
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
fitterb.hmean.Fit('response', 'B')
can2b = TCanvas()
fitterb.hsigma.SetTitle('Fitted value of Sigma barrel')
fitterb.hsigma.Draw()
eres = TF1('eres','sqrt(([0]/sqrt(x))**2+[1]**2)')
fitterb.hsigma.Fit('eres')

comp_endcap = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 200, xmin = 0, xmax = 0, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3. && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3. && simtrack_len==1 && papasjet_22_e/papasjet_e<0.01')

fittere = Fitter2D('histo2de','E_{rec}/E_{gen}vsE_{gen} endcap', 200, 5, 100, 200, 0, 2)
tree.Project('histo2de','cmsjet_e/gen_jet_e:gen_jet_e','gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3. && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01')
fittere.fit_slices()
can3e = TCanvas()
fittere.h2d.Draw()
cane = TCanvas()
fittere.hmean.SetTitle('Fitted value of mean endcap')
fittere.hmean.Draw()
responsee = TF1('responsee','[0]/(1+exp((x-[1])/[2]))')
responsee.SetParameter(0,1.)
responsee.SetParameter(1,3.)
responsee.SetParameter(2,-5.)
fittere.hmean.Fit('responsee', 'B')
can2e = TCanvas()
fittere.hsigma.SetTitle('Fitted value of Sigma endcap')
fittere.hsigma.Draw()
erese = TF1('erese','sqrt(([0]/sqrt(x))**2+[1]**2)')
fittere.hsigma.Fit('erese')
