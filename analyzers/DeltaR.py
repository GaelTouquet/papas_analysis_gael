from heppy.utils.deltar import deltaR
from heppy.framework.analyzer import Analyzer

class DeltaR(Analyzer):

    def process(self, event):
        pivot = getattr(event, self.cfg_ana.pivot)
        ptcs = getattr(event, self.cfg_ana.particles)
        dR_list = []
        if ptcs and pivot:
            pivot = pivot[0]
            for ptc in ptcs:
                dR_list.append(deltaR(pivot, ptc))
            setattr(event, 'dR_list', dR_list)
