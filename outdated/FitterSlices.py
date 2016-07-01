from cpyroot import *

class FitterSlices(Fitter2D):
    
    def __init__(self, name, tree, nx, xmin, xmax, ny, ymin, ymax, cut):
        super(FitterSlices,self).__init__(name, name,
                                          nx, xmin, xmax, ny, ymin, ymax)
        tree.Project(self.h2d.GetName(), 'jet1_rec_e/jet1_e:jet1_e', cut)
        self.fit_slices()
