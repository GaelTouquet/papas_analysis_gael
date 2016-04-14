from heppy.framework.analyzer import Analyzer
from heppy.particles.tlv.particle import Particle 
from heppy.utils.deltar import deltaR, inConeCollection
from ROOT import TLorentzVector
import math

class ConeAnalyzer(Analyzer):

    def process(self, event):
        particle = getattr(event, self.cfg_ana.particle)[0]
        rec_ptcs = getattr(event, self.cfg_ana.rec_particles)
        output = []
        if rec_ptcs:
            incone_ptcs = inConeCollection(particle, rec_ptcs, 0.3, 0.)
            for ptc in incone_ptcs:
                setattr(ptc, 'dR', deltaR(particle, ptc))
                setattr(ptc, 'gen_matched', True)
                output.append(ptc)
            tlv = TLorentzVector(particle.p4())
            tlv.SetPhi(particle.p4().Phi()+(math.pi))
            control = Particle(particle.pdgid(),
                               particle.charge(),
                               tlv)
            incontrolcone_ptcs = inConeCollection(control, rec_ptcs, 0.3, 0.)
            for ptc in incontrolcone_ptcs:
                setattr(ptc, 'dR', deltaR(control, ptc))
                setattr(ptc, 'gen_matched', False)
                output.append(ptc)
            setattr(event, self.cfg_ana.output, output)
        if hasattr(self.cfg_ana, 'pf_cone_ptcs') and hasattr(self.cfg_ana, 'control_cone_ptcs'):
            setattr(event, self.cfg_ana.pf_cone_ptcs, [ptc for ptc in output if ptc.gen_matched])
            setattr(event, self.cfg_ana.control_cone_ptcs, [ptc for ptc in output if not ptc.gen_matched])
