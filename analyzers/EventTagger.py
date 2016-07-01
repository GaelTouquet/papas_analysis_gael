from heppy.framework.analyzer import Analyzer

class EventTagger(Analyzer):

    def process(self, event):
        ptcs = []
        otherptcs = []
        pfcands = getattr(event, 'pf_cone_particles', [])
        for pfcand in pfcands:
            keep = False
            elems = []
            for h, blelems in pfcand._blocks.iteritems():
                for blelem in blelems:
                    elems.append(blelem[1])
            for h, blelems in pfcand._blocks.iteritems():
                if len(elems) != len(blelems[0][0].elements()):
                    keep = True
            if keep:
                ptcs.append(pfcand)
            else:
                otherptcs.append(pfcand)
        event.tagged_particles = ptcs
        event.nottagged_particles = otherptcs
        event.nottagged130 = False
        event.nottagged22 = False
        for ptc in otherptcs:
            if ptc.pdgid()==130:
                event.nottagged130 = True
            elif ptc.pdgid()==22:
                event.nottagged22 = True
        event.tagged130 = False
        event.tagged22 = False
        event.tagged11 = False
        event.taggedother = False
        for ptc in ptcs:
            if ptc.pdgid()==130:
                event.tagged130 = True
            elif ptc.pdgid()==22:
                event.tagged22 = True
            elif abs(ptc.pdgid())==11:
                event.tagged11 = True
            elif abs(ptc.pdgid())!=211:
                event.taggedother = True
        event.threshold_pass = False
        for ptc in ptcs:
            if ptc.pdgid()==130:
                elems = []
                for h, blelems in pfcand._blocks.iteritems():
                    for blelem in blelems:
                        elems.append(blelem[1])
                for elem in elems:
                    if elem.type()==1:
                        event.threshold_pass = True

                
