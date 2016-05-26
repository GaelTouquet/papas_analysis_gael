import os
import copy
import heppy.framework.config as cfg
import math

debug = False

if debug:
    print 'DEBUG MODE IS ON!'

from papas_analysis_gael.samples.single_cms import single_charged_hadrons, single_neutral_hadrons, single_photons

# selectedComponents = [single_charged_hadrons, single_neutral_hadrons, single_photons]

#single_neutral_hadrons.files = [single_neutral_hadrons.files[12]]
selectedComponents = [single_charged_hadrons]
single_charged_hadrons.splitFactor = 1#len(single_charged_hadrons.files)
single_neutral_hadrons.splitFactor = len(single_neutral_hadrons.files)
single_photons.splitFactor = len(single_photons.files)

from heppy.analyzers.cms.JetReader import JetReader
source = cfg.Analyzer(
    JetReader,
    gen_jets = 'ak4GenJetsNoNu',
    gen_jet_pt = 0.5, 
    jets = 'ak4PFJets', 
    jet_pt = 0.5,
    nlead = 2 
)

from papas_analysis_gael.analyzers.SimTrackReader import SimTrackReader
simtrack_reader = cfg.Analyzer(
    SimTrackReader,
    SimTrack = 'g4SimHits'
)

from papas_analysis_gael.analyzers.PFCandidateReader import PFCandidateReader
pfcandidate_reader = cfg.Analyzer(
    PFCandidateReader,
    PFCandidate = 'particleFlow'
)

from heppy.analyzers.cms.Reader import CMSReader
source_ptc = cfg.Analyzer(
    CMSReader,
    gen_particles = 'genParticles',
    pf_particles = 'particleFlow'
)

from heppy.analyzers.Filter import Filter
gen_filter = cfg.Analyzer(
    Filter,
    output = 'gen_particles_stable',
    input_objects = 'gen_particles_stable',
    filter_func = lambda x: (x.pt()<10 and abs(x.eta())<1.3)
)

from heppy.analyzers.Counter import Counter
gen_counter = cfg.Analyzer(
    Counter,
    input_objects = 'gen_particles_stable',
    min_number = 1
)

from papas_analysis_gael.analyzers.ConeAnalyzer import ConeAnalyzer
rec_cone_ana = cfg.Analyzer(
    ConeAnalyzer,
    dR = 0.3,
    pivot = 'gen_particles_stable',
    particles = 'rec_particles',
    output = 'rec_cone_particles',
    control_output = 'rec_control_cone_particles'
)

pf_cone_ana = cfg.Analyzer(
    ConeAnalyzer,
    dR = 1,
    pivot = 'gen_particles_stable',
    particles = 'pf_particles',
    output = 'pf_cone_particles',
    control_output = 'pf_control_cone_particles'
)

from papas_analysis_gael.analyzers.JetProducer import JetProducer
gen_jet = cfg.Analyzer(
    JetProducer,
    particles = 'gen_particles_stable',
    output = 'gen_jet'
)

rec_jet = cfg.Analyzer(
    JetProducer,
    particles = 'rec_cone_particles',
    output = 'rec_jet'
)

rec_control_jet = cfg.Analyzer(
    JetProducer,
    particles = 'rec_control_cone_particles',
    output = 'rec_control_jet'
)

pf_jet = cfg.Analyzer(
    JetProducer,
    particles = 'pf_cone_particles',
    output = 'pf_jet'
)

pf_control_jet = cfg.Analyzer(
    JetProducer,
    particles = 'pf_control_cone_particles',
    output = 'pf_control_jet'
)

sim_track_jet = cfg.Analyzer(
    JetProducer,
    particles = 'simtrack',
    output = 'simtrack_jet'
)

#from heppy.analyzers.JetTreeProducer import JetTreeProducer
#jet_tree = cfg.Analyzer(
#    JetTreeProducer,
#    tree_name = 'events',
#    tree_title = 'jets',
#    jets = 'gen_jets'
#    )

from papas_analysis_gael.analyzers.JetConeTreeProducer import JetConeTreeProducer
jet_cone_tree = cfg.Analyzer(
    JetConeTreeProducer,
    tree_name = 'events',
    tree_title = 'jets',
    rec_jet = 'rec_jet',
    pf_jet = 'pf_jet',
    pf_ptcs = 'pf_cone_particles',
    gen_jet = 'gen_jet',
    sim_track = 'simtracks'
    )

from heppy.analyzers.Papas import Papas
from heppy.papas.detectors.CMS import CMS
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

from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
  
if debug:
    comp = selectedComponents[0]
    comp.splitFactor =1 
    selectedComponents = [comp]



# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
    #source,
    #jet_match,
    source_ptc,
    #gen_filter,
    #gen_counter,
    simtrack_reader,
    #pfcandidate_reader,
    papas,
    rec_cone_ana,
    pf_cone_ana,
    gen_jet,
    rec_jet,
    pf_jet,
    #rec_control_jet,
    #pf_control_jet,
    #sim_track_jet,
    jet_cone_tree
    ] )

    
config = cfg.Config(
    components = selectedComponents,
    sequence = sequence,
    services = [],
    events_class = Events
)

if __name__ == '__main__':
    print config
