from ROOT import gSystem, gROOT
from ROOT import reco

def load_libs():
    print 'loading FWLite.'
    #load the libaries needed
    gSystem.Load("libFWCoreFWLite")
    gROOT.ProcessLine('FWLiteEnabler::enable();')
    gSystem.Load("libDataFormatsFWLite")
    gSystem.Load("libDataFormatsParticleFlowReco")
    #now the RootTools stuff
    # gSystem.Load("libPhysicsToolsHeppy")
    from ROOT import gInterpreter
    gInterpreter.ProcessLine("using namespace reco;")
    gInterpreter.ProcessLine("using edm::refhelper::FindUsingAdvance;")


load_libs()
from DataFormats.FWLite import Events, Handle

events = Events("/gridgroup/cms/cbernet/data/singlePiPlus_Pt100.root");

pfch  = Handle('std::vector<reco::PFCandidate>')
trackh  = Handle('std::vector<reco::Track>')
for event in events:
    print 'Event', '*'*50
    print 'PFCands', '-'*20
    event.getByLabel('particleFlow', pfch)
    for pfc in pfch.product():
        print pfc.pdgId(), pfc.pt()
        if pfc.trackRef().get():
            print '\ttrack', pfc.trackRef().get().pt()
        if abs(pfc.pdgId())==211:
            eles = pfc.elementsInBlocks()
            for ele in eles: 
                block = ele.first.get()
                print block
                eleindex = ele.second
                elements = block.elements()
                element = elements[eleindex]
                element.Dump()
                print
    print 'Tracks', '-'*20
    event.getByLabel('generalTracks', trackh)
    for track in trackh.product():
        print track.pt()
