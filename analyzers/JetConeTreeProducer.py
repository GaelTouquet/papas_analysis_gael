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
        bookJet(self.tree, 'papasjet')
        bookJet(self.tree, 'cmsjet')
        bookJet(self.tree, 'papas_control_jet')
        bookJet(self.tree, 'cms_control_jet')
        bookJet(self.tree, 'gen_jet')
        bookJet(self.tree, 'simtrack')
        var(self.tree, 'simtrack_len')
        for i in range(20):
            bookParticle(self.tree, 'simtrack_ptc'+str(i))
        bookParticle(self.tree, 'PFCandidate')

    def process(self, event):
        self.tree.reset()
        papasjet = getattr(event, self.cfg_ana.rec_jet, None)
        cmsjet = getattr(event, self.cfg_ana.pf_jet, None)
        papas_control_jet = getattr(event, self.cfg_ana.rec_control_jet, None)
        cms_control_jet = getattr(event, self.cfg_ana.pf_control_jet, None)
        gen_jet = getattr(event, self.cfg_ana.gen_jet, None)
        if papasjet:
            fillJet(self.tree, 'papasjet', papasjet)
        if cmsjet:
            fillJet(self.tree, 'cmsjet', cmsjet)
        if papas_control_jet:
            fillJet(self.tree, 'papas_control_jet', papas_control_jet)
        if cms_control_jet:
            fillJet(self.tree, 'cms_control_jet', cms_control_jet)
        if gen_jet:
            fillJet(self.tree, 'gen_jet', gen_jet)
        sim_track_jet = getattr(event, self.cfg_ana.sim_track_jet, None)
        if sim_track_jet:
            fillJet(self.tree, 'simtrack', sim_track_jet)
        sim_track_ptcs = getattr(event, self.cfg_ana.sim_track, None)
        if sim_track_ptcs:
            for i in range(min(len(sim_track_ptcs), 20)):
                fillParticle(self.tree, 'simtrack_ptc'+str(i), sim_track_ptcs[i])
        fill(self.tree, 'simtrack_len', len(sim_track_ptcs))
        pfcandidates = getattr(event, self.cfg_ana.pfcandidates, None)
        if pfcandidates:
            fillParticle(self.tree, 'PFCandidate', pfcandidates[0])
        self.tree.tree.Fill()

    def write(self, setup):
        self.rootfile.Write()
        self.rootfile.Close()
