from heppy.framework.analyzer import Analyzer
from heppy.particles.tlv.particle import Particle 
from heppy.utils.deltar import *

class ConeFinder(Analyzer):

    def process(self, event):
        gen_ptc = getattr(event, self.cfg_ana.gen_particles)[0]
        rec_ptcs = getattr(event, self.cfg_ana.rec_particles)
        if rec_ptcs != []:
            dRmax = 1e-14
            incone = inConeCollection(gen_ptc, rec_ptcs, dRmax, 0.)
            if set(incone) != set(rec_ptcs):
                event.cone_size = -1
            else:
                while incone == rec_ptcs:
                    dRmax /= 2.
                    incone = inConeCollection(gen_ptc, rec_ptcs, dRmax, 0.)
                event.cone_size = dRmax*2
        else :
            event.cone_size = -2
