from ROOT import TFile, TH1F, TCanvas, THStack, TLegend
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator
import tdrstyle

file = TFile('./Out_threshold/single_charged_hadrons/papas_analysis_gael.analyzers.JetConeTreeProducer.JetConeTreeProducer_1/jet_tree.root')
tree = file.Get('events')

previous = TH1F("previous","previous",300,0,2)
tree.Project("previous",'cmsjet_e/gen_jet_e','gen_jet_e>20 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && gen_jet_e<100')
previous.SetLineColor(4)
# previous.SetLineWidth(2)

papas = TH1F("papas","papas",300,0,2)
tree.Project("papas","papasjet_e/gen_jet_e",'gen_jet_e>20 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && gen_jet_e<100 && 130tagged==0')
papas.SetLineColor(2)
# papas.SetLineWidth(2)



can4 = TCanvas()
papas.GetXaxis().SetTitle("E_{rec}/E_{gen}")
papas.GetYaxis().SetTitle("N_{events}")
papas.Draw()
previous.Draw("same")

legend = TLegend(0.6, 0.7, 0.9, 0.9)
legend.AddEntry(papas, 'papas', 'lp')
legend.AddEntry(previous, 'GEANT4', 'lpf')
legend.SetFillColor(0)
legend.Draw('same')

# no_tagged = TH1F("no_tagged","no_tagged",300,0,2)
# tree.Project("no_tagged",'cmsjet_e/gen_jet_e','gen_jet_e>20 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && gen_jet_e<100 && 130tagged==0')
# # no_tagged.SetLineWidth(2)
# no_tagged.SetLineColor(1)

# no_22tagged = TH1F("no_22tagged","no_22tagged",300,0,2)
# tree.Project("no_22tagged",'cmsjet_e/gen_jet_e','gen_jet_e>20 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && gen_jet_e<100 && 130tagged==0 && 22tagged==0 && 130nottagged==0 && 22nottagged==0')
# # no_tagged.SetLineWidth(2)
# no_22tagged.SetLineColor(3)
# no_22tagged.Draw('same')

# test = THStack("test",300,0,2)

# electrons = TH1F("electrons","electrons",300,0,2)
# tree.Project("electrons","")
