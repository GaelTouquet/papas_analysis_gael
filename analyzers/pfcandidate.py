from heppy.particles.cms.particle import Particle
import re

class Block(object):
    
    def __init__(self, block):
        self.block = block
        
    def __hash__(self):
        tmp = re.search('<ROOT.reco::PFBlock object at (.+?)>', 
                        self.block.__repr__())
        return hash(int(tmp.group(1), 0))

    def __getattr__(self, attr):
        return getattr(self.block, attr)
        

class PFCandidate(Particle):

    def __init__(self, candidate):
        super(PFCandidate, self).__init__(candidate)
        self._elements_in_blocks = candidate.elementsInBlocks()#todo map blocks
        self._blocks = dict()
        for element in self._elements_in_blocks:
            block = Block(element.first.get())
            self._blocks.setdefault(block.__hash__(), []).append((block, block.block.elements()[element.second]))

    def print_blocks(self):
        print '-'*100
        print ' '*5, self, '\n'
        i = 1
        types = {0:'None',1:'Track',2:'PS1',3:'PS2',4:'ECAL',5:'HCAL',6:'GSF',
                 7:'BREM',8:'HFEM',9:'HFHAD',10:'SC',11:'HO',12:'kNBETypes'}
        for h in self._blocks:
            print 'Elements'+'*'*5+'\n'
            for tups in self._blocks[h]:
                print 'element', tups[1].index(), types[tups[1].type()]
                tups[1].Dump()
                print '\n'
            print 'Block '+str(i)+'*'*20+'\n'
            self._blocks[h][0][0].print_info()
            print '\n'*2
            i += 1
