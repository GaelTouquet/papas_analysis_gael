from heppy.framework.analyzer import Analyzer

class EventSearcher(Analyzer):

    def process(self, event):
        cmsjet = getattr(event, 'pf_jet', None)
        gen_jet = getattr(event, 'gen_jet', None)
        simtracks = getattr(event, 'simtracks', None)
        if cmsjet and gen_jet and simtracks:
            if cmsjet.e()/gen_jet.e()>1.1 and cmsjet.e()/gen_jet.e()<1.16 and gen_jet.pt()>1 and len(simtracks)==1 and abs(gen_jet.eta())<1.3 and gen_jet.e()<100 and cmsjet.constituents.get(211, None).e()==0:
                import pdb; pdb.set_trace()
