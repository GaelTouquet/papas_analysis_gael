from ROOT import TFile, TH2F, TCanvas, TH3F
from HistEfficiency2D import HistEfficiency2D
from style import papas_style, cms_style

papas_file = TFile('./rootfiles/papassampletuned.root')
cms_file = TFile('./rootfiles/cmssamplejetted.root')
papas_tree = papas_file.Get('events')
cms_tree = cms_file.Get('events')

#histo = TH2F('2D_eff1', 'PAPAS  efficiency : P_{T} : eta', 50, 0, 10, 50, -4, 4)

#papas_tree.Project('2D_eff1', 'jet1_eta:jet1_pt', 'jet1_pt>0')

#can1 = TCanvas()
#histo.Draw('LEGO')

#histo2 = TH2F('2D_eff2', 'PAPAS  efficiency : P_{T} : eta', 50, 0, 10, 50, -4, 4)

#papas_tree.Project('2D_eff2', 'jet1_eta:jet1_pt',
#                   'jet1_pt>0 && jet1_rec_211_num==1')

#can2 = TCanvas()
#histo2.Draw('LEGO')

#div_histo = histo2.Clone('2D_eff')

#div_histo.Divide(histo)


#can3 = TCanvas()
#div_histo.Draw('LEGO')

test = HistEfficiency2D(papas_tree,'jet1_eta:jet1_pt',
                        'jet1_pt>0',
                        'jet1_rec_211_num==1',
                        0,10,-4,4,20, papas_style, 
                        'P_{T}', 'eta', 'efficiency', 'papas')

test.draw()


test2 = HistEfficiency2D(cms_tree,'jet1_eta:jet1_pt',
                        'jet1_pt>0',
                        'jet1_rec_211_num==1',
                        0,10,-4,4,20, cms_style, 
                        'P_{T}', 'eta', 'efficiency', 'cms')

test2.draw()
