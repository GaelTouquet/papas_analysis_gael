from ROOT import TFile
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2
from papas_analysis_gael.tools.Comparator import CompHandler
from papas_analysis_gael.tools.Hist import Hist


papas_file = TFile('./rootfiles/photonspapas.root')
cms_file = TFile('./rootfiles/photonscms.root')
papas = papas_file.Get('events')
cms = cms_file.Get('events')

comp = CompHandler(papas, cms, Hist, papas_style, cms_style,
                   var = 'jet_e-gen_jet_e', 
                   cut = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1',
                   xmin = -5, xmax = 5, nbin = 100, 
                   xvar = 'E_{rec}-E_{gen}')

#integral_papas = comp.comp.plotter1.hist.ComputeIntegral()

#integral_cms = comp.comp.plotter2.hist.ComputeIntegral()

comp.change(var='control_jet_e', same = True, style2 = cms_style2)
