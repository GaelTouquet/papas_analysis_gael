from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from heppy.particles.cms.particle import Particle 

import math

class SimTrackReader(Analyzer):
    
    def declareHandles(self):
        super(SimTrackReader, self).declareHandles()
        self.handles['SimTrack'] = AutoHandle(
            self.cfg_ana.SimTrack,
            'std::vector<SimTrack>'
            )
    def process(self, event):
        self.readCollections(event.input)
        store = event.input
        simt = self.handles['SimTrack'].product()
        event.simTrack = map(Particle, simt)
