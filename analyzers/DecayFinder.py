from heppy.framework.analyzer import Analyzer

class DecayFinder(Analyzer):

    def process(self, event):
        ptcs = getattr(event, self.cfg_ana.ptcs, [])
        event.is_ecal_decay = any([hasattr(ptc,'ecal_decay') for ptc in ptcs])
