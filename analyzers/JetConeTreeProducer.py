from heppy.framework.analyzer import Analyzer
from heppy.statistics.tree import Tree
from heppy.analyzers.ntuple import *
from papas_analysis_gael.analyzers.ntuple import *
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
        # bookJet(self.tree, 'papas_control_jet')
        # bookJet(self.tree, 'cms_control_jet')
        bookJet(self.tree, 'gen_jet')
        # bookJet(self.tree, 'simtrack')
        var(self.tree, 'simtrack_len')
        var(self.tree, 'event_id')
        bookParticles(self.tree, 'tagged', 150)
        bookParticles(self.tree, 'nottagged', 150)
        var(self.tree, '130tagged')
        var(self.tree, '22tagged')
        var(self.tree, '130nottagged')
        var(self.tree, '22nottagged')
        var(self.tree, '11tagged')
        var(self.tree, 'othertagged')
        var(self.tree, 'threshold_pass')
        bookParticles(self.tree, 'cms_ptcs', 150)
        

    def process(self, event):
        self.tree.reset()
        papasjet = getattr(event, self.cfg_ana.rec_jet, None)
        cmsjet = getattr(event, self.cfg_ana.pf_jet, None)
        # papas_control_jet = getattr(event, self.cfg_ana.rec_control_jet, None)
        # cms_control_jet = getattr(event, self.cfg_ana.pf_control_jet, None)
        gen_jet = getattr(event, self.cfg_ana.gen_jet, None)
        sim_track_ptcs = getattr(event, self.cfg_ana.sim_track, None)
        cms_ptcs = getattr(event, self.cfg_ana.pf_ptcs, [])
        if papasjet:
            fillJet(self.tree, 'papasjet', papasjet)
        if cmsjet:
            fillJet(self.tree, 'cmsjet', cmsjet)
        # if papas_control_jet:
        #     fillJet(self.tree, 'papas_control_jet', papas_control_jet)
        # if cms_control_jet:
        #     fillJet(self.tree, 'cms_control_jet', cms_control_jet)
        if gen_jet:
            fillJet(self.tree, 'gen_jet', gen_jet)
        if sim_track_ptcs:
            fill(self.tree, 'simtrack_len', len(sim_track_ptcs))
        fillParticles(self.tree, 'cms_ptcs', cms_ptcs)
        fill(self.tree, 'event_id', event.input.eventAuxiliary().id().event())
        fillParticles(self.tree, 'tagged', event.tagged_particles)
        fillParticles(self.tree, 'nottagged', event.nottagged_particles)
        fill(self.tree, '130tagged', 1 if event.tagged130 else 0)
        fill(self.tree, '22tagged', 1 if event.tagged22 else 0)
        fill(self.tree, '130nottagged', 1 if event.nottagged130 else 0)
        fill(self.tree, '22nottagged', 1 if event.nottagged22 else 0)
        fill(self.tree, '11tagged', 1 if event.tagged11 else 0)
        fill(self.tree, 'othertagged', 1 if event.taggedother else 0)
        fill(self.tree, 'threshold_pass', 1 if event.threshold_pass else 0)
        self.tree.tree.Fill()
        
    def write(self, setup):
        self.rootfile.Write()
        self.rootfile.Close()
