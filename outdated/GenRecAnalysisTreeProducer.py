from heppy.framework.analyzer import Analyzer
from heppy.statistics.tree import Tree
from heppy.analyzers.ntuple import *
from heppy.utils.deltar import *

from ROOT import TFile

#def longvar( tree, varName, type=long float)

class GenRecAnalysisTreeProducer(Analyzer):
    
    def beginLoop(self, setup):
        super(GenRecAnalysisTreeProducer, self).beginLoop(setup)
        self.rootfile = TFile('/'.join([self.dirName, 'tree.root']), 'recreate')
        self.tree = Tree('RecGen', '')
        bookParticle(self.tree, 'gen_ptc')
        for i in range(5):
            bookParticle(self.tree, 'rec_ptc{j}'.format(j=i))
        bookJet(self.tree, 'rec_jet')
        bookJet(self.tree, 'gen_jet')
        var(self.tree, 'n_photons')
        var(self.tree, 'n_PI')
        var(self.tree, 'n_K0')
        var(self.tree, 'n_other')
        var(self.tree, 'n_rec_ptc')
        var(self.tree, 'event_gen_E')
        var(self.tree, 'event_rec_E')
        var(self.tree, 'iev')
        var(self.tree, 'cone_size')

    def process(self, event):
        gen_particle = getattr(event, self.cfg_ana.gen_particles)[0]
        #rec_particles = sorted(inConeCollection(
        #        gen_particle,
        #        getattr(event, self.cfg_ana.rec_particles),
        #        2
        #        ),
        #                       key = lambda x: x.e())
        rec_particles = sorted(getattr(event, self.cfg_ana.rec_particles),
                               key = lambda x: x.e())
        self.tree.reset()
        fillParticle(self.tree, 'gen_ptc', gen_particle)
        nphotons, npi, nk0, nother, nrecptc, gen_E, rec_E = [0]*7
        gen_E = gen_particle.e()
        for ptc in rec_particles:
            rec_E += ptc.e()
        for i in range(min(len(rec_particles), 5)):
            fillParticle(self.tree, 'rec_ptc{j}'.format(j=i), rec_particles[i])
            pdgid = abs(rec_particles[i].pdgid())
            nrecptc+=1
            if pdgid == 211:
                npi+=1
            elif pdgid == 22:
                nphotons+=1
            elif pdgid == 130:
                nk0+=1
            else :
                nother+=1
        fill(self.tree, 'n_photons', nphotons)
        fill(self.tree, 'n_PI', npi)
        fill(self.tree, 'n_K0', nk0)
        fill(self.tree, 'n_other', nother)
        fill(self.tree, 'n_rec_ptc', nrecptc)
        fill(self.tree, 'event_gen_E', gen_E)
        fill(self.tree, 'event_rec_E', rec_E)
        fill(self.tree, 'iev', getattr(event, 'iEv'))
        if rec_particles == []:
            fill(self.tree,'cone_size', -1.)
        else :
            fill(self.tree,
                 'cone_size', 
                 max([deltaR(gen_particle, rec_ptc) for rec_ptc in rec_particles])
                 )
        rec_jet = getattr(event, self.cfg_ana.rec_jet)
        if rec_jet:
            fillJet(self.tree, 'rec_jet', rec_jet[0])
            if hasattr(rec_jet[0], 'match') and rec_jet[0].match is not None:
                fillJet(self.tree, 'gen_jet', rec_jet[0].match)
        self.tree.tree.Fill()

    def write(self, setup):
        self.rootfile.Write()
        self.rootfile.Close()
