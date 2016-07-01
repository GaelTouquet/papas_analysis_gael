from ROOT import TFile, TCanvas, gDirectory
from HistDivider import histdivider

file = TFile('./rootfiles/cmssample.root')
tree = file.Get('events')

#tree.Project('h_pt_rec', 'jet1_pt', 'jet1_e>0')
#tree.Project('h_pt_rectrack', 'jet1_pt', 'jet1_e>0 && jet1_rec_211_num==1')
#h_pt_rec = gDirectory.Get('h_pt_rec')
#h_pt_rectrack = gDirectory.Get('h_pt_rectrack')
#h_pt_rectrack.Divide(h_pt_rec)
#h_pt_rectrack.SetTitle('efficiency : pt')
#h_pt_rectrack.SetStats(False)
#a = TCanvas()
#h_pt_rectrack.Draw()

can1 = TCanvas()
cut1, cut2 = 'jet1_e>0 && jet1_rec_211_num==1', 'jet1_e>0'
histdivider(tree, 'efficiency : pt', 'jet1_pt', cut1, cut2).Draw()

tree.Project('h_pt_rec_lowpt', 'jet1_pt', 'jet1_e>0 && jet1_pt<10')
tree.Project('h_pt_rectrack_lowpt', 'jet1_pt', 
             'jet1_e>0 && jet1_rec_211_num==1 && jet1_pt<10')
h_pt_rec_lowpt = gDirectory.Get('h_pt_rec_lowpt')
h_pt_rectrack_lowpt = gDirectory.Get('h_pt_rectrack_lowpt')
h_pt_rectrack_lowpt.Divide(h_pt_rec_lowpt)
h_pt_rectrack_lowpt.SetTitle('efficiency : low pt')
h_pt_rectrack_lowpt.SetStats(False)
m = TCanvas()
h_pt_rectrack_lowpt.Draw()


tree.Project('h_e_rec_lowe', 'jet1_e', 'jet1_e>0 && jet1_e<10')
tree.Project('h_e_rectrack_lowe', 'jet1_e', 
             'jet1_e>0 && jet1_rec_211_num==1 && jet1_e<10')
h_e_rec_lowe = gDirectory.Get('h_e_rec_lowe')
h_e_rectrack_lowe = gDirectory.Get('h_e_rectrack_lowe')
h_e_rectrack_lowe.Divide(h_e_rec_lowe)
h_e_rectrack_lowe.SetTitle('efficiency : low e')
h_e_rectrack_lowe.SetStats(False)
m2 = TCanvas()
h_e_rectrack_lowe.Draw()



tree.Project('h_eta_rec', 'jet1_eta', 'jet1_e>0')
tree.Project('h_eta_rectrack', 'jet1_eta', 'jet1_e>0 && jet1_rec_211_num==1')
h_eff_eta = gDirectory.Get('h_eta_rectrack')
h_eff_eta.Divide(gDirectory.Get('h_eta_rec'))
h_eff_eta.SetTitle('efficiency : eta')
h_eff_eta.SetStats(False)
d = TCanvas()
h_eff_eta.Draw()




tree.Project('h_pt_receta', 'jet1_pt', 'jet1_e>0 && abs(jet1_eta)<2.4')
tree.Project('h_pt_rectracketa', 'jet1_pt', 
             'jet1_e>0 && jet1_rec_211_num==1 && abs(jet1_eta)<2.4')
h_pt_receta = gDirectory.Get('h_pt_receta')
h_pt_rectracketa = gDirectory.Get('h_pt_rectracketa')
h_pt_rectracketa.Divide(h_pt_receta)
h_pt_rectracketa.SetTitle('efficiency : pt {abs(eta)<2.4}')
h_pt_rectracketa.SetStats(False)
o = TCanvas()
h_pt_rectracketa.Draw()


tree.Project('h_lowpt_receta', 'jet1_pt',
             'jet1_e>0 && abs(jet1_eta)<2.4 && jet1_pt<10')
tree.Project('h_lowpt_rectracketa', 'jet1_pt', 
             'jet1_e>0 && jet1_rec_211_num==1 && abs(jet1_eta)<2.4 && jet1_pt<10')
h_lowpt_receta = gDirectory.Get('h_lowpt_receta')
h_lowpt_rectracketa = gDirectory.Get('h_lowpt_rectracketa')
h_lowpt_rectracketa.Divide(h_lowpt_receta)
h_lowpt_rectracketa.SetTitle('efficiency : low pt {abs(eta)<2.4}')
h_lowpt_rectracketa.SetStats(False)
l = TCanvas()
h_lowpt_rectracketa.Draw()


o2 = TCanvas()
tree.Draw('jet1_rec_pt','jet1_rec_pt<10 && jet1_rec_pt>0')
