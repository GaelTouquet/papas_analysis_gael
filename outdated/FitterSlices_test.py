from ROOT import TFile, TCanvas, TCut, TF1, TH1F, TH2F, gDirectory
from cpyroot import *
import sys

class FitterSlices(Fitter2D):
    
    def __init__(self, name, tree, nx, xmin, xmax, ny, ymin, ymax, cut):
        super(FitterSlices,self).__init__(name, name,
                                          nx, xmin, xmax, ny, ymin, ymax)
        tree.Project(self.h2d.GetName(), 'jet1_rec_e/jet1_e:jet1_e', cut)
        print self.h2d.GetName()
        self.fit_slices()


particles = sys.argv[1]
f = TFile('./rootfiles/sample_{ptcs}.root'.format(ptcs=particles))
tree = f.Get('jets')
rec = 'jet1_rec_e>0 && jet1_e>0'
a = TCanvas()
h = TH2F('h','h',200,0.5,1000.,100,0.,1.5)
tree.Project(h.GetName(),'jet1_rec_e/jet1_e:jet1_e',rec)
h.Draw()

for i in range(200):
    proj = h.ProjectionY('', i, i, '')
    proj.Draw()
#j = FitterSlices('histo',tree,200,0.5,1000,100,0.,1.5,rec)
#b = TCanvas()
#j.hsigma.Draw()
