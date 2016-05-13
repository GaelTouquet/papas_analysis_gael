from heppy.framework.analyzer import Analyzer
from heppy.statistics.tree import Tree
from heppy.analyzers.ntuple import *
from papas_analysis_gael.analyzers.ntuple import *
from ROOT import TFile

class SimTrackTreeProducer(Analyzer):

    def beginLoop(self, setup):
        super(SimTrackTreeProducer, self).beginLoop(setup)
        self.rootfile = TFile('/'.join([self.dirName,
                                        'jet_tree.root']),
                              'recreate')
        self.tree = Tree( self.cfg_ana.tree_name,
                          self.cfg_ana.tree_title )
        bookSimTrack(self.tree, 'simtrack')
        var(self.tree, 'simtrack_len')

    def process(self, event):
        simtracks = getattr(event, self.cfg_ana.simtracks)
        for simtrack in simtracks:
            self.tree.reset()
            fillSimTrack(self.tree, 'simtrack', simtrack)
            fill(self.tree, 'simtrack_len', len(simtracks))
            self.tree.tree.Fill()

    def write(self, setup):
        self.rootfile.Write()
        self.rootfile.Close()
