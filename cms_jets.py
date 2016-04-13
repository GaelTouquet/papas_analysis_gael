import os
import copy
import heppy.framework.config as cfg

debug = False

if debug:
    print 'DEBUG MODE IS ON!'

comp = cfg.Component(
    'singlepi',
    #files = ['/gridgroup/cms/cbernet/data/singleK0L.root']
    #files = ['/gridgroup/cms/cbernet/data/singlePhoton.root']
    files = ['/gridgroup/cms/cbernet/data/singlePi_50k.root']
)

selectedComponents = [comp]

from heppy.analyzers.cms.JetReader import JetReader
source = cfg.Analyzer(
    JetReader,
    gen_jets = 'ak4GenJetsNoNu',
    gen_jet_pt = 0.5, 
    jets = 'ak4PFJets', 
    jet_pt = 0.5,
    nlead = 2 
)

from heppy.analyzers.cms.Reader import CMSReader
source_ptc = cfg.Analyzer(
    CMSReader,
    gen_particles = 'genParticles',
    pf_particles = 'particleFlow'
)

from ConeAnalyzer import ConeAnalyzer
cone_ana = cfg.Analyzer(
    ConeAnalyzer,
    particle = 'gen_particles_stable',
    rec_particles = 'rec_particles',
    output = 'coned_ptcs',
    pf_cone_ptcs = 'rec_cone_ptcs',
    control_cone_ptcs = 'control_cone_ptcs'
)



from heppy.analyzers.fcc.JetClusterizer import JetClusterizer
pf_jets = cfg.Analyzer(
    JetClusterizer,
    instance_label = 'pf_jets',
    output = 'pf_jets',
    particles = 'pf_particles',
    fastjet_args = dict( ptmin = 0.1)
)

rec_jets = cfg.Analyzer(
    JetClusterizer,
    instance_label = 'rec_jets',
    output = 'rec_jets',
    particles = 'rec_particles',
    fastjet_args = dict( ptmin = 0.1)
)

rec_cone_jets = cfg.Analyzer(
    JetClusterizer,
    instance_label = 'rec_cone_jets',
    output = 'rec_cone_jets',
    particles = 'rec_cone_ptcs',
    fastjet_args = dict( ptmin = 0.1)
)



gen_jets = cfg.Analyzer(
    JetClusterizer,
    instance_label = 'gen_jets',
    output = 'gen_jets',
    particles = 'gen_particles_stable',
    fastjet_args = dict( ptmin = 0.1)
)


pf_cone_jets = cfg.Analyzer(
    JetClusterizer,
    instance_label = 'pf_cone_jets',
    output = 'pf_cone_jets',
    particles = 'pf_cone_ptcs',
    fastjet_args = dict( ptmin = 0.01)
)

control_cone_jets = cfg.Analyzer(
    JetClusterizer,
    instance_label = 'control_cone_jets',
    output = 'control_cone_jets',
    particles = 'control_cone_ptcs',
    fastjet_args = dict( ptmin = 0.01)
)

from heppy.analyzers.Matcher import Matcher
jet_match = cfg.Analyzer(
    Matcher,
    instance_label = 'jet_match',
    match_particles = 'pf_jets',
    particles = 'gen_jets',
    delta_r = 0.3
    )

ptc_match = cfg.Analyzer(
    Matcher,
    instance_label = 'ptc_match',
    match_particles = 'pf_particles',
    particles = 'gen_particles',
    delta_r = 0.3
    )

from heppy.analyzers.JetTreeProducer import JetTreeProducer
jet_tree = cfg.Analyzer(
    JetTreeProducer,
    tree_name = 'events',
    tree_title = 'jets',
    jets = 'gen_jets'
    )

from JetPtcTreeProducer import JetPtcTreeProducer
tree = cfg.Analyzer(
    JetPtcTreeProducer,
    tree_name = 'events',
    tree_title = 'jets',
    jets = 'gen_jets',
    particle = 'gen_particles'
    )

from PapasTreeProducer import PapasTreeProducer
papas_tree = cfg.Analyzer(
    PapasTreeProducer,
    tree_name = 'events',
    tree_title = 'jets',
    jets = 'gen_jets'
    )

from ConeTreeProducer import ConeTreeProducer
cone_tree = cfg.Analyzer(
    ConeTreeProducer,
    tree_name = 'ptcs',
    tree_title = 'particles',
    particles = 'coned_ptcs'
)

from JetConeTreeProducer import JetConeTreeProducer
jet_cone_tree = cfg.Analyzer(
    JetConeTreeProducer,
    tree_name = 'events',
    tree_title = 'jets',
    jet = 'rec_cone_jets',
    control_jet = 'control_cone_jets',
    gen_jet = 'gen_jets'
    )

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

from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
  
if debug:
    comp = selectedComponents[0]
    comp.splitFactor =1 
    selectedComponents = [comp]



# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
    source_ptc,
    papas,
    cone_ana,
    gen_jets,
    rec_cone_jets,
    control_cone_jets,
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
