from heppy.framework.analyzer import Analyzer
from heppy.statistics.tree import Tree
from heppy.analyzers.ntuple import *

from ROOT import TFile

class GenRecTreeProducer(Analyzer):
    
    def beginLoop(self, setup):
        super(GenRecTreeProducer, self).beginLoop(setup)
        self.rootfile = TFile('/'.join([self.dirName, 'tree.root']), 'recreate')
        self.tree = Tree('RecGen', '')
        for i in range(5):
            bookParticle(self.tree, 'gen_ptc{j}'.format(j=i))
            bookParticle(self.tree, 'rec_ptc{j}'.format(j=i))
        var(self.tree, 'nb_gen_ptc')
        var(self.tree, 'nb_rec_ptc')
        var(self.tree, 'event_gen_E')
        var(self.tree, 'event_rec_E')
        var(self.tree, 'iev')

    def process(self, event):
        gen_particles = sorted(getattr(event, self.cfg_ana.gen_particles),
                               key = lambda x: x.e())
        rec_particles = sorted(getattr(event, self.cfg_ana.rec_particles),
                               key = lambda x: x.e())

        self.tree.reset()
        for i in range(min(len(gen_particles), 5)):
            fillParticle(self.tree, 'gen_ptc{j}'.format(j=i), gen_particles[i])
        for i in range(min(len(rec_particles), 5)):
            fillParticle(self.tree, 'rec_ptc{j}'.format(j=i), rec_particles[i])
        fill(self.tree, 'nb_gen_ptc', len(gen_particles))
        fill(self.tree, 'nb_rec_ptc', len(rec_particles))
        gen_E, rec_E = 0, 0
        for ptc in gen_particles:
            gen_E += ptc.e()
        for ptc in rec_particles:
            rec_E += ptc.e()
        fill(self.tree, 'event_gen_E', gen_E)
        fill(self.tree, 'event_rec_E', rec_E)
        fill(self.tree, 'iev', getattr(event, 'iEv'))
        self.tree.tree.Fill()

    def write(self, setup):
        self.rootfile.Write()
        self.rootfile.Close()
