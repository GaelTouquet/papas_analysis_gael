from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from heppy.particles.cms.particle import Particle 

class PFCandidateReader(Analyzer):
    
    def declareHandles(self):
        super(PFCandidateReader, self).declareHandles()
        self.handles['PFCandidate'] = AutoHandle(
            self.cfg_ana.PFCandidate,
            'std::vector<reco::PFCandidate>'
            )
        #self.handles['Clusters'] = AutoHandle(
        #    self.cfg_ana.PFCandidate,

    def process(self, event):
        self.readCollections(event.input)
        store = event.input
        pfcand = self.handles['PFCandidate'].product()
        pfcandidates = map(Particle, pfcand)
        event.pfcandidates = sorted( pfcandidates,
                                    key = lambda ptc: ptc.e(), reverse=True )
