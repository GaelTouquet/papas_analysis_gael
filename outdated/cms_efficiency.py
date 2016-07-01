from ROOT import TFile, TCanvas
from HistDivider import histdivider
import sys

if len(sys.argv)==2:
    opt = sys.argv[1]
else:
    opt = ''

File = TFile('./rootfiles/cmssample{option}.root'.format(option=opt))

tree = File.Get('events')


cut1, cut2 = 'jet1_e>0 && jet1_rec_211_num==1', 'jet1_e>0'
can1 = TCanvas()
histdivider(tree, 'efficiency : pt', 'jet1_pt', cut1, cut2).Draw()

cut1 = 'jet1_e>0 && jet1_rec_211_num==1 && jet1_pt<3'
cut2 = 'jet1_e>0 && jet1_pt<3'
can2 = TCanvas()
histdivider(tree, 'efficiency : low pt', 'jet1_pt', cut1, cut2).Draw()

cut1 = 'jet1_e>0 && jet1_rec_211_num==1 && jet1_e<3'
cut2 = 'jet1_e>0 && jet1_e<3'
can3 = TCanvas()
histdivider(tree, 'efficiency : low e', 'jet1_e', cut1, cut2).Draw()
