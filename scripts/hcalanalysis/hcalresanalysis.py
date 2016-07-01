from ROOT import TFile, TH2F, TCanvas, TF1
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator
from cpyroot.tools.fitter2d import Fitter2D
import tdrstyle

fil2 = TFile('./rootfiles/neutral_hadron_tree.root')
tree2 = fil2.Get('events')

# comp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
#                       nbin = 200, xmin = 0, xmax = 5, xvar = 'E_{rec}/E_{gen}',
#                       var1 = 'cmsjet_e/gen_jet_e', 
#                       cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01',
#                       var2 = 'papasjet_e/gen_jet_e',
#                       cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.01')

fitterb = Fitter2D('histo2db','E_{rec}/E_{gen}vsE_{gen} barrel', 100, 12, 100, 200, 0, 2)
tree2.Project('histo2db','cmsjet_e/gen_jet_e:gen_jet_e','gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01')
fitterb.fit_slices(selection=3)
can3b = TCanvas()
fitterb.h2d.Draw()

can2b = TCanvas()
fitterb.hsigma.SetTitle('Fitted value of Sigma barrel')
fitterb.hsigma.GetXaxis().SetTitle('E_{gen} (GeV)')
fitterb.hsigma.GetYaxis().SetTitle('#sigma')
#fitterb.hsigma.SetStats(0)
fitterb.hsigma.Draw()
eres = TF1('eres','sqrt(([0]/sqrt(x))**2+([1]/x)**2+[2]**2)')
eres.SetParName(0, 'a')
eres.SetParName(1, 'b')
eres.SetParName(2, 'c')
print 'fit of Eres in barrel'
fitterb.hsigma.Fit('eres')



# fitterbp = Fitter2D('histo2dbp','E_{rec}/E_{gen}vsE_{gen} barrel', 50, 12, 50, 200, 0, 2)
# tree2.Project('histo2dbp','papasjet_e/gen_jet_e:gen_jet_e','gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.01')
# fitterbp.fit_slices()
# can3bp = TCanvas()
# fitterbp.h2d.Draw()
# canbp = TCanvas()
# fitterbp.hmean.SetTitle('Fitted value of mean barrel')
# fitterbp.hmean.GetXaxis().SetTitle('E_{gen} (GeV)')
# fitterbp.hmean.GetYaxis().SetTitle('#mu')
# fitterbp.hmean.SetStats(0)
# fitterbp.hmean.Draw()
# responsep = TF1('responsep','[0]/(1+exp((x-[1])/[2]))')
# response.SetParameter(0,1.)
# response.SetParameter(1,3.)
# response.SetParameter(2,-5.)
# fitterb.hmean.Fit('response', 'B'# )
# can2bp = TCanvas()
# fitterbp.hsigma.SetTitle('Fitted value of Sigma barrel')
# fitterbp.hsigma.GetXaxis().SetTitle('E_{gen} (GeV)')
# fitterbp.hsigma.GetYaxis().SetTitle('#sigma')
# fitterbp.hsigma.SetStats(0)
# fitterbp.hsigma.Draw()

# canb = TCanvas()
# fitterb.hmean.SetTitle('Fitted value of mean barrel')
# fitterb.hmean.GetXaxis().SetTitle('E_{gen} (GeV)')
# fitterb.hmean.GetYaxis().SetTitle('#mu')
# fitterb.hmean.SetStats(0)
# fitterb.hmean.Draw()
# response = TF1('response','[0]/(1+exp((x-[1])/[2]))')
# response.SetParameter(0,1.)
# response.SetParameter(1,3.)
# response.SetParameter(2,-5.)
# fitterb.hmean.Fit('response', 'B')
# # # comp_endcap = HistComparator(tree, style1 = cms_style, style2 = papas_style,
# # #                       nbin = 200, xmin = 0, xmax = 0, xvar = 'E_{rec}/E_{gen}',
# # #                       var1 = 'cmsjet_e/gen_jet_e', 
# # #                       cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3. && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01',
# # #                       var2 = 'papasjet_e/gen_jet_e',
# # #                       cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3. && simtrack_len==1 && papasjet_22_e/papasjet_e<0.01')

fittere = Fitter2D('histo2de','E_{rec}/E_{gen}vsE_{gen} endcap', 100, 12, 100, 200, 0, 2)
tree2.Project('histo2de','cmsjet_e/gen_jet_e:gen_jet_e','gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3. && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01')
fittere.fit_slices(selection=3)
can3e = TCanvas()
fittere.h2d.Draw()
cane = TCanvas()
fittere.hmean.SetTitle('Fitted value of mean endcap')
fittere.hmean.GetXaxis().SetTitle('E_{gen} (GeV)')
fittere.hmean.GetYaxis().SetTitle('#mu')
fittere.hmean.SetStats(0)
fittere.hmean.Draw()
responsee = TF1('responsee','[0]/(1+exp((x-[1])/[2]))')
responsee.SetParameter(0,1.)
responsee.SetParameter(1,3.)
responsee.SetParameter(2,-5.)
fittere.hmean.Fit('responsee', 'B')
can2e = TCanvas()
fittere.hsigma.SetTitle('Fitted value of Sigma endcap')
fittere.hsigma.GetXaxis().SetTitle('E_{gen} (GeV)')
fittere.hsigma.GetYaxis().SetTitle('#sigma')
#fittere.hsigma.SetStats(0)
fittere.hsigma.Draw()
erese = TF1('erese','sqrt(([0]/sqrt(x))**2+([1]/x)**2+[2]**2)')
erese.SetParName(0, 'a')
erese.SetParName(1, 'b')
erese.SetParName(2, 'c')
print 'fit of Eres in endcap'
erese.SetParameter(0, 1.2310019064740882)
erese.SetParameter(1, 0.0)
erese.SetParameter(2, 0.18197050066505263)
#erese.SetParLimits(1, 0.0, 1.)
erese.SetRange(0.,100.)
fittere.hsigma.Fit('erese', 'B R')

# # comp_erec_egen = HistComparator(tree, style1 = cms_style, 
# #                                   style2 = papas_style,
# #                       nbin = 200, xmin = 0, xmax = 2.5, xvar = 'E_{rec}/E_{gen}',
# #                       var1 = 'cmsjet_e/gen_jet_e', 
# #                       cut = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && gen_jet_e>10 && gen_jet_e<100',
# #                       var2 = 'papasjet_e/gen_jet_e')

# # comp_erec_egen_noecalhit = HistComparator(tree, style1 = cms_style, 
# #                                   style2 = papas_style,
# #                       nbin = 200, xmin = 0, xmax = 2.5, xvar = 'E_{rec}/E_{gen}',
# #                       var1 = 'cmsjet_e/gen_jet_e', 
# #                       cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01 && gen_jet_e>10 && gen_jet_e<100',
# #                       var2 = 'papasjet_e/gen_jet_e',
# #                                 cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.01 && gen_jet_e>10 && gen_jet_e<100')


# # #print 'cms integral :', comp_erec_egen_noecalhit.hist1.Integral()
# # #print 'papas integral :', comp_erec_egen_noecalhit.hist2.Integral()

# # comp_erec_egen_noecalhit_endcap = HistComparator(tree, style1 = cms_style, 
# #                                   style2 = papas_style,
# #                       nbin = 200, xmin = 0, xmax = 2.5, xvar = 'E_{rec}/E_{gen}',
# #                       var1 = 'cmsjet_e/gen_jet_e', 
# #                       cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<2.93 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01 && gen_jet_e>10 && gen_jet_e<100',
# #                       var2 = 'papasjet_e/gen_jet_e',
# #                                 cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<2.93 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.01 && gen_jet_e>10 && gen_jet_e<100')
