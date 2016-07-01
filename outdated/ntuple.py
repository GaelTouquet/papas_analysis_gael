#!/bin/env python

from heppy.analyzers.ntuple import *
import math

def bookVect(tree, varName, nmax, type = float):
    tree.var('n_'+varName, type = int)
    tree.vector(varName, 'n_'+varName, nmax, type=type)

def fillVect(tree, varName, var_iterable):
    tree.fill('n_'+varName, len(var_iterable))
    tree.vfill(varName, var_iterable)

def bookVector3(tree, vName):
    var(tree, '{vName}_x'.format(vName=vName))
    var(tree, '{vName}_y'.format(vName=vName))
    var(tree, '{vName}_z'.format(vName=vName))
    var(tree, '{vName}_rho'.format(vName=vName))

def fillVector3(tree, vName, v3):
    fill(tree, '{vName}_x'.format(vName=vName), v3.x())
    fill(tree, '{vName}_y'.format(vName=vName), v3.y())
    fill(tree, '{vName}_z'.format(vName=vName), v3.z())
    fill(tree, '{vName}_rho'.format(vName=vName), math.sqrt(v3.x()**2+v3.y()**2))

def bookSimTrack(tree, stName):
    bookParticle(tree, stName)
    bookVector3(tree, '{stName}_vertex'.format(stName=stName))

def fillSimTrack(tree, stName, simtrack):
    fillParticle(tree, stName, simtrack)
    fillVector3(tree, '{stName}_vertex'.format(stName=stName), simtrack.vertex())
