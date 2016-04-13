from Hist import Hist
from ROOT import TFile, TCanvas
from style import papas_style, cms_style
from HistHandler import HistHandler

basecut = 'jet1_pt>1 && jet1_pt<10 && jet1_rec_pt>0 && abs(jet1_eta)<1.3'

cms_file = TFile('./rootfiles/cmssamplejetted.root')
cms = cms_file.Get('events')

args = {'var' : 'jet1_rec_e/jet1_e',
        'cut' : basecut,
        'xmin' : 0, 'xmax' : 3, 'nbin' : 100,
        'xvar' : 'E_{rec}/E_{gen}'}

hist = HistHandler(cms, cms_style,
                   var = 'jet1_rec_e/jet1_e',
                   cut = basecut,
                   xmin = 0, xmax = 3, nbin = 100,
                   xvar = 'E_{rec}/E_{gen}')
hist.Draw()
hist.canvas[0].SetLogy()
hist.change(cutadd = 'jet1_rec_211_e/jet1_rec_e<1', log = True)
hist.change(cutadd = 'jet1_rec_211_e>0', log = True)
