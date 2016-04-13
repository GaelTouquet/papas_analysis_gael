from ROOT import TFile
from HistEfficiency import HistEfficiency
from style import papas_style, cms_style
from Comparator import CompHandler
from Hist import Hist

papas_file = TFile('./rootfiles/papassampletuned2.root')
cms_file = TFile('./rootfiles/cmssamplejetted.root')
papas = papas_file.Get('events')
cms = cms_file.Get('events')

eff_eta = CompHandler(papas, cms, HistEfficiency, papas_style, cms_style,
                      var = 'jet1_eta', cut = 'jet1_pt>1 && jet1_pt<10',
                      eff_cut = 'jet1_rec_211_num==1', 
                      xmin = -3, xmax = 3, nbin = 100, varname = 'eta')

energy = CompHandler(papas, cms, Hist, papas_style, cms_style,
                     var = 'jet1_rec_e/jet1_e', cut = 'jet1_pt>1 && jet1_pt<10',
                     xmin = 0, xmax = 3, nbin = 100, 
                     varname = 'E_{rec}/E_{gen}')
