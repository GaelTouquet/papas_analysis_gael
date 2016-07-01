import os
import copy
import heppy.framework.config as cfg
import math


debug = False

if debug:
    print 'DEBUG MODE IS ON!'

from papas_analysis_gael.samples.single_cms import single_charged_hadrons, single_neutral_hadrons, single_photons

# selectedComponents = [single_charged_hadrons, single_neutral_hadrons, single_photons]

selectedComponents = [single_neutral_hadrons]
single_charged_hadrons.splitFactor = len(single_charged_hadrons.files)

from heppy.analyzers.cms.Reader import CMSReader
source_ptc = cfg.Analyzer(
    CMSReader,
    gen_particles = 'genParticles',
    pf_particles = 'particleFlow'
)

from papas_analysis_gael.analyzers.SimTrackReader import SimTrackReader
simtrack_reader = cfg.Analyzer(
    SimTrackReader,
    SimTrack = 'g4SimHits',
    SimVertex = 'g4SimHits'
)

from heppy.analyzers.Filter import Filter
gen_filter = cfg.Analyzer(
    Filter,
    output = 'gen_particles_stable',
    input_objects = 'gen_particles_stable',
    filter_func = lambda x: (x.pt()>1 and x.pt()<100)
)

from heppy.analyzers.Counter import Counter
gen_counter = cfg.Analyzer(
    Counter,
    input_objects = 'gen_particles_stable',
    min_number = 1
)

from papas_analysis_gael.analyzers.SimTrackTreeProducer import SimTrackTreeProducer
tree = cfg.Analyzer(
    SimTrackTreeProducer,
    tree_name = 'simtracks',
    tree_title = 'simtracks',
    simtracks = 'simtracks'
)

from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
  
if debug:
    comp = selectedComponents[0]
    comp.splitFactor =1 
    selectedComponents = [comp]



# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
    source_ptc,
    gen_filter,
    gen_counter,
    simtrack_reader,
    tree
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
