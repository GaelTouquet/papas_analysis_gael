from ROOT import TFile, TCanvas
from HistEfficiency import HistEfficiency
from cpyroot.tools.style import *

fil = TFile('./rootfiles/papassample.root')

pteffhist = HistEfficiency(fil.Get('events'),
                           'jet1_pt',
                           'jet1_pt>0',
                           'jet1_rec_211_num==1',
                           100,0,1,
                           sBlue)

pteffhist.draw()

e_effhist = HistEfficiency(fil.Get('events'),
                           'jet1_e',
                           'jet1_pt>0',
                           'jet1_rec_211_num==1',
                           100,0,10,
                           sBlue)
e_effhist.draw()

eta_effhist = HistEfficiency(fil.Get('events'),
                             'jet1_eta',
                             'jet1_pt>0',
                             'jet1_rec_211_num==1',
                             100,-3,3,
                             sBlue)

eta_effhist.draw()
