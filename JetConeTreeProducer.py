from heppy.framework.analyzer import Analyzer
from heppy.statistics.tree import Tree
from heppy.analyzers.ntuple import *
from heppy.particles.tlv.jet import Jet

from ROOT import TFile, TLorentzVector

class JetConeTreeProducer(Analyzer):

    def beginLoop(self, setup):
        super(JetConeTreeProducer, self).beginLoop(setup)
        self.rootfile = TFile('/'.join([self.dirName,
                                        'jet_tree.root']),
                              'recreate')
        self.tree = Tree( self.cfg_ana.tree_name,
                          self.cfg_ana.tree_title )
        bookJet(self.tree, 'jet')
        bookJet(self.tree, 'control_jet')
        bookJet(self.tree, 'gen_jet')

    def process(self, event):
        self.tree.reset()
        jet = getattr(event, self.cfg_ana.jet, [])
        control_jet = getattr(event, self.cfg_ana.control_jet, [])
        gen_jet = getattr(event, self.cfg_ana.gen_jet, [])
        if jet:
            fillJet(self.tree, 'jet', jet[0])
        if control_jet:
            fillJet(self.tree, 'control_jet', control_jet[0])
        if gen_jet:
            fillJet(self.tree, 'gen_jet', gen_jet[0])
        self.tree.tree.Fill()

    def write(self, setup):
        self.rootfile.Write()
        self.rootfile.Close()
