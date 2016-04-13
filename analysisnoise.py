from ROOT import TFile
from style import papas_style, cms_style, cms_style2
from Comparator import CompHandler
from Hist import Hist


papas_file = TFile('./rootfiles/JetConeanalysisPapas.root')
cms_file = TFile('./rootfiles/JetConeanalysis.root')
papas = papas_file.Get('events')
cms = cms_file.Get('events')

comp = CompHandler(papas, cms, Hist, papas_style, cms_style,
                   var = 'jet_e-gen_jet_e', 
                   cut = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1',
                   xmin = 0, xmax = 2.5, nbin = 50, 
                   xvar = 'E_{rec}-E_{gen}')

comp.canvas[0].SetLogy()

comp.change(var='control_jet_e', same = True, style2 = cms_style2)


#comp.change(var='jet1_rec_e-jet1_e', cut='jet1_pt>1 && jet1_pt<10 && abs(jet1_eta)<1.3', xmin=-10, xmax=20, nbin=100, log=True)
