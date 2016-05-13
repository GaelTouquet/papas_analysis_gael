from heppy.framework.analyzer import Analyzer
from heppy.particles.tlv.particle import Particle 
from heppy.utils.deltar import deltaR, inConeCollection
from ROOT import TLorentzVector
import math

class ConeAnalyzer(Analyzer):

    def process(self, event):
        pivot = getattr(event, self.cfg_ana.pivot)[0]
        ptcs = getattr(event, self.cfg_ana.particles)
        dR = self.cfg_ana.dR
        cone_ptcs = inConeCollection(pivot, ptcs, dR, 0.)
        for ptc in cone_ptcs:
            setattr(ptc, 'dR', deltaR(pivot, ptc))
        tlv = TLorentzVector(pivot.p4())
        tlv.SetPhi(pivot.p4().Phi()+math.pi)
        tlv_theta = math.pi-pivot.p4().Theta()
        if tlv_theta >= math.pi: 
            tlv_theta -= math.pi
        tlv.SetTheta(tlv_theta)
        control_pivot = Particle(pivot.pdgid(),
                                 pivot.charge(),
                                 tlv)
        control_cone_ptcs = inConeCollection(control_pivot, ptcs, dR, 0.)
        setattr(event, self.cfg_ana.output, cone_ptcs)
        setattr(event, self.cfg_ana.control_output, control_cone_ptcs)
