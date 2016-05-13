from heppy.particles.particle import Particle as BaseParticle
from ROOT import TLorentzVector, TVector3
import math

class Vertex(object):
    
    def __init__(self, vertex):
        self.vertex = TVector3(vertex.position().x(),
                               vertex.position().y(),
                               vertex.position().z())

    def __getattr__(self, attr): 
        return getattr(self.vertex, attr)

    def __str__(self):
        tmp = 'vertex : x = {vertx}, y = {verty}, z = {vertz}, rho = {rho}'
        return tmp.format(
            vertx = self.vertex.x(),
            verty = self.vertex.y(),
            vertz = self.vertex.z(),
            rho = math.sqrt(self.vertex.x()**2+self.vertex.y()**2))

class SimTrack(BaseParticle):
    def __init__(self, simtrack, simvertex=None):
        self.simtrack = simtrack
        self._charge = simtrack.charge()
        self._pid = simtrack.type()
        self._status = 1
        self._tlv = TLorentzVector()
        p4 = simtrack.momentum()
        self._tlv.SetPtEtaPhiM(p4.pt(), p4.eta(), p4.phi(), p4.mass())
        if simvertex:
            self._vertex = Vertex(simvertex)
        else:
            self._vertex = None
        
    def vertex(self):
        return self._vertex
        
    def __getattr__(self, attr): 
        return getattr(self.simtrack, attr)

    def __str__(self):
        tmp = '{className} : pdgid = {pdgid:5}, status = {status:3}, q = {q:2} {p4}, {vertex}'
        return tmp.format(
            className = self.__class__.__name__,
            pdgid = self.pdgid(),
            status = self.status(),
            q = self.q(),
            p4 = super(BaseParticle, self).__str__(),
            vertex = self._vertex.__str__() if self.vertex else ''
            )

    def __repr__(self):
        return str(self)
