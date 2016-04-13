while len(loop.event.rec_particles)<2:
    if loop.event.iEv%10==0: print loop.event.iEv
    next()
for ptc in loop.event.rec_particles:
    print 'rec :', ptc, '\n'
print 'gen :', loop.event.gen_particles, '\n'
print simulator.pfsequence.pfreco.links.elements

while loop.event.iEv<59:
    if loop.event.iEv%100==0: print loop.event.iEv
    next()
