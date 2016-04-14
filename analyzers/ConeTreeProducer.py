from heppy.framework.analyzer import Analyzer
from heppy.statistics.tree import Tree
from heppy.analyzers.ntuple import *

from ROOT import TFile

class ConeTreeProducer(Analyzer):

    def beginLoop(self, setup):
        super(ConeTreeProducer, self).beginLoop(setup)
        self.rootfile = TFile('/'.join([self.dirName,
                                        'jet_tree.root']),
                              'recreate')
        self.tree = Tree( self.cfg_ana.tree_name,
                          self.cfg_ana.tree_title )
        bookParticle(self.tree, 'particle')
        var(self.tree, 'dR')
        var(self.tree, 'is_gen_matched')
        var(self.tree, 'iEv')

    def process(self, event):
        ptcs = getattr(event, self.cfg_ana.particles, [])
        fill(self.tree, 'iEv', getattr(event, 'iEv'))
        for ptc in ptcs:
            self.tree.reset()
            fillParticle(self.tree, 'particle', ptc)
            if ptc.gen_matched:
                fill(self.tree, 'is_gen_matched', 1)
            else:
                fill(self.tree, 'is_gen_matched', 0)
            fill(self.tree, 'dR', ptc.dR)
            self.tree.tree.Fill()

    def write(self, setup):
        self.rootfile.Write()
        self.rootfile.Close()

