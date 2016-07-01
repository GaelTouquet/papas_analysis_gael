from ROOT import TFile, TH2F, TCanvas, TF1
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator
from cpyroot.tools.fitter2d import Fitter2D
import tdrstyle

def ymax(h1=None, h2=None):
    '''Returns the best y axis maximum so that h1 and h2 are both visible.'''
    def getmax(h):
        return  h.GetBinContent(h.GetMaximumBin())
    ymax = max(getmax(h1), getmax(h2))
    if ymax == 0:
        ymax = 1
    return ymax

canvas = []

fil = TFile('./rootfiles/neutral_hadron_test_tree2.root')
tree = fil.Get('events')

fittercms = Fitter2D('histocms','cms', 100, 0, 100, 200, 0, 2)
tree.Project('histocms','cmsjet_e/gen_jet_e:gen_jet_e','gen_jet_pt>1 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01')
fittercms.fit_slices()

fitterpapas = Fitter2D('histopapas','papas', 100, 0, 100, 200, 0, 2)
tree.Project('histopapas','papasjet_e/gen_jet_e:gen_jet_e','gen_jet_pt>1 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.01')
fitterpapas.fit_slices()

selection = 0

for i in range(20):
   canvas.append(TCanvas())
   hist = getattr(fittercms, '{name}hslice{i}'.format(i=i, name=fittercms.h2d.GetName()))
   cms_style.formatHisto(hist)
   hist.SetTitle('Ebin = {i} to {j} Gev'.format(i=i, j=i+1))
   histpapas = getattr(fitterpapas, '{name}hslice{i}'.format(i=i, name=fitterpapas.h2d.GetName()))
   papas_style.formatHisto(histpapas)
   hist.Draw()
   histpapas.Draw('same')
   hist.GetYaxis().SetRangeUser(0.1, ymax(hist, histpapas)*1.2)
   mean = hist.GetMean()
   sigma = hist.GetRMS()
   func = TF1('fitgauss','gaus')
   if selection:
       func.SetRange(mean-(selection*sigma), mean+(selection*sigma))
       func.SetParLimits(2, 0, selection*sigma)
   func.SetParameter(1, mean)
   func.SetParameter(2, sigma)
   hist.Fit('fitgauss', 'O B')
    

# comp_erec_egen = HistComparator(tree, style1 = cms_style, 
#                                   style2 = papas_style,
#                       nbin = 200, xmin = 0, xmax = 2.5, xvar = 'E_{rec}/E_{gen}',
#                       var1 = 'cmsjet_e/gen_jet_e', 
#                       cut = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && gen_jet_e>10 && gen_jet_e<100',
#                       var2 = 'papasjet_e/gen_jet_e')

# comp_erec_egen_noecalhit = HistComparator(tree, style1 = cms_style, 
#                                   style2 = papas_style,
#                       nbin = 200, xmin = 0, xmax = 2.5, xvar = 'E_{rec}/E_{gen}',
#                       var1 = 'cmsjet_e/gen_jet_e', 
#                       cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01 && gen_jet_e>10 && gen_jet_e<100',
#                       var2 = 'papasjet_e/gen_jet_e',
#                                 cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)<1.3 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.01 && gen_jet_e>10 && gen_jet_e<100')


# #print 'cms integral :', comp_erec_egen_noecalhit.hist1.Integral()
# #print 'papas integral :', comp_erec_egen_noecalhit.hist2.Integral()

# comp_erec_egen_noecalhit_endcap = HistComparator(tree, style1 = cms_style, 
#                                   style2 = papas_style,
#                       nbin = 200, xmin = 0, xmax = 2.5, xvar = 'E_{rec}/E_{gen}',
#                       var1 = 'cmsjet_e/gen_jet_e', 
#                       cut1 = 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<2.93 && simtrack_len==1 && cmsjet_22_e/cmsjet_e<0.01 && gen_jet_e>10 && gen_jet_e<100',
#                       var2 = 'papasjet_e/gen_jet_e',
#                                 cut2 = 'gen_jet_pt>0 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<2.93 && simtrack_len==1 && papasjet_22_e/papasjet_e<0.01 && gen_jet_e>10 && gen_jet_e<100')
