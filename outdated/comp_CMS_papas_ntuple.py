from ROOT import TFile, TCanvas, TCut, TF1, TH1F, gDirectory
import sys


particles = sys.argv[1]
f = TFile('./rootfiles/sample_{ptcs}.root'.format(ptcs=particles))
hjets = f.Get('jets')
rec = TCut('jet1_rec_e>0 && jet1_e>0')
a = TCanvas()
hjets.Draw('jet1_rec_e/jet1_e:jet1_e>>h("h","h",99,1,100)',rec)
h = gDirectory.Get('h')
gaus = TF1('gaus','gaus')
h.FitSlicesY(gaus)
mean = gDirectory.Get('h_1')
b = TCanvas()
mean.Draw()
sigma = gDirectory.Get('h_2')
c = TCanvas()
sigma.Draw()
const = gDirectory.Get('h_0')
d = TCanvas()
const.Draw()
