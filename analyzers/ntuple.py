from heppy.analyzers.ntuple import *

def vect( tree, varName, len_var, max_len, type=float ):
    """Books a variable sized vector in tree.
    - varName : name given in the tree for the booked vector variable
    - len_var : an int variable that needs to be booked in the tree that informs on the vector length at each iteration
    - maxlen : an int that gives the maximum size of the booked vector
    - type : the type of the variables in the booked vector
    """
    tree.vector( varName, len_var, maxlen=max_len, type=type )

def vfill( tree, varName, values ):
    """Fills the booked vector with varName name. 
    values must be an iterable.
    See vect( tree, varName, len_var, type=float ) func for more details.
    """
    tree.vfill( varName, values )

def bookParticles( tree, particles_name, max_len ):
    """Books variable sized vectors for each particle variables with max_len maximum length and will be referenced as particles_name_{variable} in the tree. 
    Also books a variable for the length of the vector.
    """
    var(tree, particles_name+'_len', type=int)
    vect(tree, '{particles_name}_pdgid'.format(particles_name=particles_name),
         particles_name+'_len', max_len)
    vect(tree, '{particles_name}_e'.format(particles_name=particles_name),
         particles_name+'_len', max_len)
    vect(tree, '{particles_name}_pt'.format(particles_name=particles_name),
         particles_name+'_len', max_len)
    vect(tree, '{particles_name}_theta'.format(particles_name=particles_name),
         particles_name+'_len', max_len)
    vect(tree, '{particles_name}_eta'.format(particles_name=particles_name),
         particles_name+'_len', max_len)
    vect(tree, '{particles_name}_phi'.format(particles_name=particles_name),
         particles_name+'_len', max_len)
    vect(tree, '{particles_name}_m'.format(particles_name=particles_name),
         particles_name+'_len', max_len)
    vect(tree, '{particles_name}_dR'.format(particles_name=particles_name),
         particles_name+'_len', max_len)

def fillParticles( tree, particles_name, particles ):
    """Fills the particles_name named booked particle variable vectors with variables in particles.
    See bookParticles func for more details
    """
    fill(tree, particles_name+'_len', len(particles))
    variables = {'pdgid':[], 'e':[], 'pt':[], 'theta':[], 'eta':[], 'phi':[], 'm':[], 'dR':[]}
    for ptc in particles:
        variables['pdgid'].append(ptc.pdgid())
        variables['e'].append(ptc.e())
        variables['pt'].append(ptc.pt())
        variables['theta'].append(ptc.theta())
        variables['eta'].append(ptc.eta())
        variables['phi'].append(ptc.phi())
        variables['m'].append(ptc.m())
        variables['dR'].append(ptc.dR)
    vfill(tree, '{particles_name}_pdgid'.format(particles_name=particles_name),
         variables['pdgid'])
    vfill(tree, '{particles_name}_e'.format(particles_name=particles_name),
         variables['e'])
    vfill(tree, '{particles_name}_pt'.format(particles_name=particles_name),
         variables['pt'])
    vfill(tree, '{particles_name}_theta'.format(particles_name=particles_name),
         variables['theta'])
    vfill(tree, '{particles_name}_eta'.format(particles_name=particles_name),
         variables['eta'])
    vfill(tree, '{particles_name}_phi'.format(particles_name=particles_name),
         variables['phi'])
    vfill(tree, '{particles_name}_m'.format(particles_name=particles_name),
         variables['m'])
    vfill(tree, '{particles_name}_dR'.format(particles_name=particles_name),
         variables['dR'])
