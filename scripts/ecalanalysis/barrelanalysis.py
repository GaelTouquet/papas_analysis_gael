from ROOT import TFile, TCanvas, TF1
from papas_analysis_gael.tools.style import papas_style, cms_style
from papas_analysis_gael.tools.HistComparator import HistComparator
from cpyroot.tools.fitter2d import Fitter2D
import tdrstyle

fil = TFile('./rootfiles/photons.root')
tree = fil.Get('events')

comp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 300, xmin = 0.8, xmax = 1.2, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut = 'gen_jet_pt>10 && gen_jet_e<100 && abs(gen_jet_eta)<1.479 && simtrack_len==3')

fitter = Fitter2D('histo2d','E_{rec}/E_{gen}vsE_{gen} barrel', 100, 0, 100, 200, 0, 2)
tree.Project('histo2d','cmsjet_e/gen_jet_e:gen_jet_e','gen_jet_e>1 && gen_jet_e<100 && abs(gen_jet_eta)<1.479 && simtrack_len==3')
fitter.fit_slices()
can1 = TCanvas()
fitter.h2d.Draw()
fitter.hsigma.SetTitle('Fitted value of Sigma HCAL Barrel')
fitter.hsigma.GetXaxis().SetTitle('E_{gen} (GeV)')
fitter.hsigma.GetYaxis().SetTitle('#sigma')
can2 = TCanvas()
fitter.hsigma.Draw()
eres = TF1('eres','sqrt(([0]/sqrt(x))**2+([1]/x)**2+[2]**2)')
eres.SetParName(0, 'a(#sigma)')
eres.SetParName(1, 'b(#sigma)')
eres.SetParName(2, 'c(#sigma)')
fitter.hsigma.Fit('eres')
fitter.hmean.SetTitle('Fitted value of mu HCAL Barrel')
fitter.hmean.GetXaxis().SetTitle('E_{gen} (GeV)')
fitter.hmean.GetYaxis().SetTitle('#mu')
can4 = TCanvas()
fitter.hmean.Draw()
response = TF1('response','[0]/(1+exp((x-[1])/[2]))')
response.SetParameter(0,1.)
response.SetParameter(1,3.)
response.SetParameter(2,-5.)
response.SetParName(0, 'a(#mu)')
response.SetParName(1, 'b(#mu)')
response.SetParName(2, 'c(#mu)')
fitter.hmean.Fit('response')
