from ROOT import TFile
from papas_analysis_gael.tools.style import papas_style, cms_style
from papas_analysis_gael.tools.Comparator import CompHandler
from papas_analysis_gael.tools.Hist import Hist
import tdrstyle

papas_file = TFile('./rootfiles/papassampletuned2.root')
cms_file = TFile('./rootfiles/cmssamplejetted.root')
papas = papas_file.Get('events')
cms = cms_file.Get('events')

basecut = 'jet1_pt>1 && jet1_pt<10 && jet1_rec_pt>0'

anacut = basecut + ' && jet1_rec_e/jet1_e>1.05 && jet1_rec_e/jet1_e<1.2'

testcut = anacut + ' && jet1_rec_211_num==1'

comp = CompHandler(papas, cms, Hist, papas_style, cms_style,
                     var = 'jet1_rec_e/jet1_e', 
                     cut = basecut,
                     xmin = 0, xmax = 3, nbin = 100, 
                     xvar = 'E_{rec}/E_{gen}')

comp.canvas[0].SetLogy()

comp.change(cutadd = 'abs(jet1_eta)<1.3', log = True)

comp.change(cutadd = 'jet1_rec_211_e/jet1_rec_e<1', log = True)

comp.change(cutadd = 'jet1_rec_211_e>0', log = True)

#comp_pt = CompHandler(papas, cms, Hist, papas_style, cms_style,
#                   var = 'jet1_rec_pt/jet1_pt', cut = 'jet1_pt>1 && jet1_pt<10'#,
#                   xmin = 0, xmax = 3, nbin = 100, 
#                   varname = 'E_{rec}/E_{gen}')
#
#comp_pt.canvas[0].SetLogy()


