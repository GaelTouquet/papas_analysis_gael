from ROOT import TFile, TH2F, TCanvas, TF1
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator
from cpyroot.tools.fitter2d import Fitter2D
import tdrstyle

fil = TFile('./rootfiles/photon_tree.root')
tree = fil.Get('events')

eres = TF1('eres', 'sqrt(([0]/sqrt(x))**2+([1]/x)**2+[2]**2)')

comp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 200, xmin = 0.5, xmax = 1.5, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.479 && simtrack_len==3',
                      var2 = 'papasjet_e/gen_jet_e')

# comp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
#                       nbin = 200, xmin = 0.7, xmax = 1.3, xvar = 'E_{rec}/E_{gen}',
#                       var1 = 'cmsjet_e/gen_jet_e', 
#                       cut = 'gen_jet_pt>1 && abs(gen_jet_eta)<1.479 && simtrack_len==3',
#                       var2 = 'papasjet_e/gen_jet_e')

# comp2 = HistComparator(tree, style1 = cms_style, style2 = papas_style,
#                       nbin = 200, xmin = 0.6, xmax = 1.4, xvar = 'E_{rec}/E_{gen}',
#                       var1 = 'cmsjet_e/gen_jet_e', 
#                       cut = 'gen_jet_pt>1 && abs(gen_jet_eta)>1.479 && abs(gen_jet_eta)<3 && simtrack_len==3',
#                       var2 = 'papasjet_e/gen_jet_e')

fitter = Fitter2D('histo2d','E_{rec}/E_{gen}vsE_{gen} endcap', 198, 5, 100, 200, 0, 2)
tree.Project('histo2d','cmsjet_e/gen_jet_e:gen_jet_e','gen_jet_pt>1 && abs(gen_jet_eta)>1.479 && abs(gen_jet_eta)<3 && simtrack_len==3 && cmsjet_e>0')
fitter.fit_slices(selection=3)
can3 = TCanvas()
fitter.h2d.Draw()
can = TCanvas()
fitter.hmean.SetTitle('Fitted value of mean endcap')
fitter.hmean.GetXaxis().SetTitle('E_{gen} (GeV)')
fitter.hmean.GetYaxis().SetTitle('#mu')
fitter.hmean.SetStats(0)
fitter.hmean.Draw()
fitter.hsigma.SetTitle('Fitted value of Sigma endcap')





fitterb = Fitter2D('histo2db','E_{rec}/E_{gen}vsE_{gen} barrel', 198, 1, 100, 200, 0, 2)
tree.Project('histo2db','cmsjet_e/gen_jet_e:gen_jet_e','gen_jet_pt>1 && abs(gen_jet_eta)<1.479 && simtrack_len==3 && cmsjet_e>0')
fitterb.fit_slices(selection=2)
can3b = TCanvas()
fitterb.h2d.Draw()
canb = TCanvas()
fitterb.hmean.SetTitle('Fitted value of mean barrel')
fitterb.hmean.GetXaxis().SetTitle('E_{gen} (GeV)')
fitterb.hmean.GetYaxis().SetTitle('#mu')
fitterb.hmean.SetStats(0)

fitterb.hmean.Draw()
can2b = TCanvas()
fitterb.hsigma.SetTitle('Fitted value of Sigma barrel')
fitterb.hsigma.GetXaxis().SetTitle('E_{gen} (GeV)')
fitterb.hsigma.GetYaxis().SetTitle('#sigma')
fitterb.hsigma.SetStats(0)

fitterb.hsigma.Draw()
eres.SetParameter(0,0.073)
eres.SetParameter(1,0.1)
eres.SetParameter(2,0.005)
fitterb.hsigma.Fit('eres','B')


can2 = TCanvas()
fitter.hsigma.GetXaxis().SetTitle('E_{gen} (GeV)')
fitter.hsigma.GetYaxis().SetTitle('#sigma')
fitter.hsigma.SetStats(0)
fitter.hsigma.Draw()
eres.SetParameter(0,0.073)
eres.SetParameter(1,0.1)
eres.SetParameter(2,0.005)
fitter.hsigma.Fit('eres','B')


#comp3 = HistComparator(tree, style1 = cms_style, style2 = papas_style,
#                      nbin = 200, xmin = 0, xmax = 2, xvar = 'E_{rec}/E_{gen}',
#                      var1 = 'cmsjet_e/gen_jet_e', 
#                      cut = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)>1.479 && abs(gen_jet_eta)<3 && simtrack_len==3 && gen_jet_e>',
#                      var2 = 'papasjet_e/gen_jet_e')
