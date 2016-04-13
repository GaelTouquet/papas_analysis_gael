import os
import copy
import heppy.framework.config as cfg

import logging
# next 2 lines necessary to deal with reimports from ipython
logging.shutdown()
reload(logging)
logging.basicConfig(level=logging.WARNING)

comp = cfg.Component(
    'singlepi',
    files = ['/gridgroup/cms/cbernet/data/singlePi_50k.root']
)
selectedComponents = [comp]

import math

#TODO colin debug this! 
from heppy.analyzers.Gun import Gun
source = cfg.Analyzer(
    Gun,
    pdgid = 211,
    thetamin = -1.5,
    thetamax = 1.5,
    ptmin = 0.1,
    ptmax = 10,
    flat_pt = True,
)  

from heppy.analyzers.cms.Reader import CMSReader
source_ptc = cfg.Analyzer(
    CMSReader,
    gen_particles = 'genParticles',
    pf_particles = 'particleFlow'
)

from ROOT import gSystem
# gSystem.Load("libdatamodelDict")
# from EventStore import EventStore as Events
from heppy.framework.eventsgen import Events

from heppy.analyzers.Papas import Papas
from heppy.papas.detectors.TunedCMS import CMS
papas = cfg.Analyzer(
    Papas,
    instance_label = 'papas',
    detector = CMS(),
    gen_particles = 'gen_particles_stable',
    sim_particles = 'sim_particles',
    rec_particles = 'rec_particles',
    display = False,
    verbose = True
)

#from heppy.analyzers.PapasPFBlockBuilder import PapasPFBlockBuilder
#pfblocks = cfg.Analyzer(
#    PapasPFBlockBuilder
#)

# and then particle reconstruction from blocks 

#added by Gael

#from GenRecTreeProducer import GenRecTreeProducer
#tree = cfg.Analyzer(
#    GenRecTreeProducer,
#    instance_label = 'GenRec',
#    gen_particles = 'gen_particles_stable',
#    rec_particles = 'rec_particles'
#)

#from GenRecAnalysisTreeProducer import GenRecAnalysisTreeProducer
#anatree = cfg.Analyzer(
#    GenRecAnalysisTreeProducer,
#    instance_label = 'GenRecAna',
#    gen_particles = 'gen_particles_stable',
#    rec_particles = 'rec_particles',
#    gen_jet = 'gen_jets',
#    rec_jet = 'rec_jets'
#)

from JetPtcTreeProducer import JetPtcTreeProducer
jet_tree = cfg.Analyzer(
    JetPtcTreeProducer,
    jets = 'gen_jets',
    tree_name = 'events',
    tree_title = 'events',
    particle = 'gen_particles'
)

from heppy.analyzers.fcc.JetClusterizer import JetClusterizer
rec_jets = cfg.Analyzer(
    JetClusterizer,
    instance_label = 'rec_jets',
    output = 'rec_jets',
    particles = 'rec_particles',
    fastjet_args = dict( ptmin = 0.1)
)

pf_jets = cfg.Analyzer(
    JetClusterizer,
    instance_label = 'pf_jets',
    output = 'pf_jets',
    particles = 'pf_particles',
    fastjet_args = dict( ptmin = 0.1)
)


gen_jets = cfg.Analyzer(
    JetClusterizer,
    instance_label = 'gen_jets',
    output = 'gen_jets',
    particles = 'gen_particles_stable',
    fastjet_args = dict( ptmin = 0.1)
)

from heppy.analyzers.Matcher import Matcher
jets_matcher = cfg.Analyzer(
    Matcher,
    instance_label = 'jet_match',
    delta_r = 0.3,
    match_particles = 'rec_jets',
    particles = 'gen_jets'
)

ptc_match = cfg.Analyzer(
    Matcher,
    instance_label = 'ptc_match',
    match_particles = 'rec_particles',
    particles = 'gen_particles',
    delta_r = 0.3
    )

from PapasTreeProducer import PapasTreeProducer
papas_tree = cfg.Analyzer(
    PapasTreeProducer,
    tree_name = 'events',
    tree_title = 'jets',
    jets = 'gen_jets'
    )


#from ConeFinder import ConeFinder
#conefinder = cfg.Analyzer(
#    ConeFinder,
#    gen_particles = 'gen_particles_stable',
#    rec_particles = 'rec_particles'
#)

#from heppy.analyzers.ParticleTreeProducer import ParticleTreeProducer
#Treetest = cfg.Analyzer(

# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
    source,
    papas,
    gen_jets,
    rec_jets,
    jets_matcher,
    papas_tree
    ] )
 
config = cfg.Config(
    components = selectedComponents,
    sequence = sequence,
    services = [],
    events_class = Events
)

if __name__ == '__main__':
    import sys
    from heppy.framework.looper import Looper

    import random
    random.seed(0xdeadbeef)

    def process(iev=None):
        if iev is None:
            iev = loop.iEvent
        loop.process(iev)
        if display:
            display.draw()

    def next():
        loop.process(loop.iEvent+1)
        if display:
            display.draw()            

    iev = None
    if len(sys.argv)==2:
        papas.display = True
        iev = int(sys.argv[1])
        
    loop = Looper( 'looper', config,
                   nEvents=1000,
                   nPrint=0,
                   timeReport=True)
    simulation = None
    for ana in loop.analyzers: 
        if hasattr(ana, 'display'):
            simulation = ana
    display = getattr(simulation, 'display', None)
    simulator = getattr(simulation, 'simulator', None)
    if simulator: 
        detector = simulator.detector
    if iev is not None:
        process(iev)
    else:
        loop.loop()
        loop.write()
