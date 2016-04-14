from ROOT import TFile, TCanvas, TCut, TF1, TH1F, gDirectory, TObjArray
from cpyroot import *
import sys


particles = sys.argv[1]
f = TFile('./rootfiles/sample_{ptcs}.root'.format(ptcs=particles))
tree = f.Get('jets')
rec = TCut('jet1_rec_e>0 && jet1_e>0')
a = TCanvas()
if particles == 'h0':
    tree.Draw('jet1_rec_e/jet1_e:jet1_e>>h(200,0.5,1000.,100,0.,3.5)',rec)
elif particles == 'photon':
    tree.Draw('jet1_rec_e/jet1_e:jet1_e>>h(200,0.5,1000.,1000,0.,1.5)',rec)
elif particles == 'photon_low_e':
    tree.Draw('jet1_rec_e/jet1_e:jet1_e>>h(200,0.5,100.,500,0.,1.5)',rec)
h = gDirectory.Get('h')
arr = TObjArray()
gaus = TF1('gaus','gaus')
h.FitSlicesY(gaus)
mean = gDirectory.Get('h_1')
b = TCanvas()
mean.Draw()
sigma = gDirectory.Get('h_2')
c = TCanvas()
sigma.Draw()
if particles == 'photon':
    Ecal_res = TF1('Ecal_res',
                   'sqrt((([0]/(sqrt(x)))**2)+(([1]/x)**2)+([2]**2))',
                   0.5, 1000)
    sigma.Fit('Ecal_res', "", "", 0.5, 1000)
elif particles == 'photon_low_e':
    Ecal_res = TF1('Ecal_res',
                   'sqrt((([0]/(sqrt(x)))**2)+(([1]/x)**2)+([2]**2))',
                   1., 100.)
    sigma.Fit('Ecal_res', "", "", 5., 100.)
elif particles == 'h0':
    Hcal_res = TF1('Hcal_res',
                   '[0]/(sqrt(x))',
                   0.5, 1000)
    sigma.Fit('Hcal_res', "", "", 20, 1000)

chi_2 = gDirectory.Get('h_chi2')
d = TCanvas()
chi_2.Draw()
