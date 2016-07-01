from ROOT import TFile, TCanvas, gStyle
from HistHandler import HistHandler
from cpyroot import *


file1 = TFile('./rootfiles/cmssample.root')
file2 = TFile('./rootfiles/cmssamplejetted.root')
tree1 = file1.Get('events')
tree2 = file2.Get('events')

first_hists = [{'title': 'energy', 'var': 'jet1_e', 'cut': 'jet1_e>0'},
               {'title': 'rec_energy', 'var': 'jet1_e', 
                'cut': 'jet1_e>0 && jet1_rec_211_num==1'}
               ]

handler = HistHandler(tree1, first_hists)

#handler.show_hist('energy')
#handler.show_hist('low_energy')

#a = TCanvas()
#handler.hists['energy'].Draw()
#b = TCanvas()
#handler.hists['rec_energy'].Draw()

#comparator = HistComparator('test', handler.hists['rec_energy'], handler.hists['energy'])
#comparator.draw()

officialStyle(gStyle)

#handler.hist_compare('_efficiency:e', 'n_h^{#pm}', 'n_rec_h^{#pm}==1', 'jet1_e', 'jet1_e>0 && jet1_rec_211_num==1', 'jet1_e>0', True)
#handler.hist_compare('efficiency:pt', 'n_h^{#pm}', 'n_rec_h^{#pm}==1', 'jet1_pt', 'jet1_e>0 && jet1_rec_211_num==1', 'jet1_e>0', True)

handler.compare_trees('efficiency:e', tree2, 'jet1_pt', 'jet1_pt>0 && jet1_pt<10', True)
