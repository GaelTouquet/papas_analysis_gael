from ROOT import TFile, TH2F, TCanvas

fil = TFile('./rootfiles/neutral_hadron_simtrack.root')
tree = fil.Get('simtracks')

track_all = TH2F('track_all','vertices',2000,-1200,1200,200,0,200)
tree.Project('track_all','simtrack_vertex_rho:simtrack_vertex_z','')
track_all.SetStats(0)
can1 = TCanvas()
track_all.Draw()

ecal_vertices = TH2F('ecal_vertices','vertices',2000,-1200,1200,200,0,200)
tree.Project('ecal_vertices','simtrack_vertex_rho:simtrack_vertex_z','simtrack_len==1')
ecal_vertices.SetStats(0)
can2 = TCanvas()
ecal_vertices.Draw()
