from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from papas_analysis_gael.analyzers.simtrack import SimTrack 


class SimTrackReader(Analyzer):
    
    def declareHandles(self):
        super(SimTrackReader, self).declareHandles()
        self.handles['SimTrack'] = AutoHandle(
            self.cfg_ana.SimTrack,
            'std::vector<SimTrack>'
            )
        if hasattr(self.cfg_ana, 'SimVertex'):
            self.handles['SimVertex'] = AutoHandle(
                self.cfg_ana.SimVertex,
                'std::vector<SimVertex>'
                )


    def process(self, event):
        self.readCollections(event.input)
        store = event.input
        simts = self.handles['SimTrack'].product()
        if hasattr(self.cfg_ana, 'SimVertex'):
            simvs = self.handles['SimVertex'].product()
        simtracks = []
        for simt in simts:
            if hasattr(self.cfg_ana, 'SimVertex'):
                vertices = [vertex for vertex in simvs if vertex.vertexId()==simt.vertIndex()]
                if len(vertices)!=1:
                    import pdb; pdb.set_trace()
                simtracks.append(SimTrack(simt,vertices[0]))
            else:
                simtracks.append(SimTrack(simt))
        event.simtracks = simtracks
