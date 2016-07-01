from ROOT import TFile, TH1F, TCanvas
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator

file = TFile('./rootfiles/charged_hadron_tree4.root')
tree = file.Get('events')

Erec_Egen = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                           nbin = 500, xmin = 0., xmax = 3., 
                           xvar = 'E_{rec}/E_{gen}',
                           var1 = 'cmsjet_e/gen_jet_e',
                           cut = 'gen_jet_e>20 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && gen_jet_e<100',
                           var2 = 'papasjet_e/gen_jet_e')
Erec_Egen.canva.SetLogy()

no_region = TH1F("no_region","no region",300,0,2)
tree.Project("no_region","cmsjet_e/gen_jet_e","gen_jet_e>20 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && gen_jet_e<100 && (cmsjet_e/gen_jet_e<1.03 || cmsjet_e/gen_jet_e>1.3)")
region_no130 = TH1F("region_no130","region_no130",300,0,2)
tree.Project("region_no130","cmsjet_e/gen_jet_e","gen_jet_e>20 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && gen_jet_e<100 && cmsjet_e/gen_jet_e>1.03 && cmsjet_e/gen_jet_e<1.3 && tagged_pdgid!=130")
region_corrected = TH1F("region_corrected","region_corrected",300,0,2)
tree.Project("region_corrected","(cmsjet_e-tagged_e)/gen_jet_e","gen_jet_e>20 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && gen_jet_e<100 && cmsjet_e/gen_jet_e>1.03 && cmsjet_e/gen_jet_e<1.3 && tagged_pdgid==130")

total = TH1F("total","total",300,0,2)
total.Add(no_region, region_no130)
total.Add(region_corrected)
total.SetLineColor(1)
can0 = TCanvas()

previous = TH1F("previous","previous",300,0,2)
tree.Project("previous",'cmsjet_e/gen_jet_e','gen_jet_e>20 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && gen_jet_e<100')
previous.SetLineColor(4)
# previous.SetLineWidth(2)

papas = TH1F("papas","papas",300,0,2)
tree.Project("papas","papasjet_e/gen_jet_e",'gen_jet_e>20 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && gen_jet_e<100 && tagged_len==0')
papas.SetLineColor(2)
# papas.SetLineWidth(2)
papas.Draw()
previous.Draw("same")
total.Draw("same")


can4 = TCanvas()
papas.GetXaxis().SetTitle("E_{rec}/E_{gen}")
papas.Draw()
previous.Draw("same")
no_tagged = TH1F("no_tagged","no_tagged",300,0,2)
tree.Project("no_tagged",'cmsjet_e/gen_jet_e','gen_jet_e>20 && simtrack_len==1 && abs(gen_jet_eta)<1.3 && gen_jet_e<100 && tagged_len==0')
# no_tagged.SetLineWidth(2)
no_tagged.SetLineColor(1)
no_tagged.Draw("same")
