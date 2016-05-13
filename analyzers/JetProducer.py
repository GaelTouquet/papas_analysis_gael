from heppy.framework.analyzer import Analyzer
from heppy.particles.tlv.jet import Jet
from heppy.particles.jet import JetConstituents
from ROOT import TLorentzVector

class JetProducer(Analyzer):

    def process(self, event):
        ptcs = getattr(event, self.cfg_ana.particles)
        if ptcs:
            tlv = TLorentzVector()
            for ptc in ptcs:
                tlv += ptc.p4()
            jet = Jet(tlv)
            jet.constituents = JetConstituents()
            for ptc in ptcs:
                jet.constituents.append(ptc)
            jet.constituents.sort()
            setattr(event, self.cfg_ana.output, jet)
