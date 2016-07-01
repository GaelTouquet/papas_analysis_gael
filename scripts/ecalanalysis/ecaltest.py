from ROOT import TFile
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator
import tdrstyle

fil = TFile('Out_old/single_photons/papas_analysis_gael.analyzers.JetConeTreeProducer.JetConeTreeProducer_1/jet_tree.root')
#fil = TFile('Out_new/single_photons/papas_analysis_gael.analyzers.JetConeTreeProducer.JetConeTreeProducer_1/jet_tree.root')
tree = fil.Get('events')

comp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 300, xmin = 0.8, xmax = 1.2, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_e>20 && gen_jet_e<100 && abs(gen_jet_eta)<1.3 && simtrack_len==3',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_e>20 && gen_jet_pt<100 && abs(gen_jet_eta)<1.3 && simtrack_len==3')

fil2 = TFile('Out_new/single_photons/papas_analysis_gael.analyzers.JetConeTreeProducer.JetConeTreeProducer_1/jet_tree.root')
tree2 = fil2.Get('events')

comp2 = HistComparator(tree2, style1 = cms_style, style2 = papas_style,
                      nbin = 300, xmin = 0.8, xmax = 1.2, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_e>20 && gen_jet_e<100 && abs(gen_jet_eta)<1.3 && simtrack_len==3',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_e>20 && gen_jet_pt<100 && abs(gen_jet_eta)<1.3 && simtrack_len==3')

comp3 = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 300, xmin = 0.8, xmax = 1.2, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_e>20 && gen_jet_e<100 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3 && simtrack_len==3',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_e>20 && gen_jet_pt<100 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3 && simtrack_len==3')

comp23 = HistComparator(tree2, style1 = cms_style, style2 = papas_style,
                      nbin = 300, xmin = 0.8, xmax = 1.2, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_e>20 && gen_jet_e<100 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3 && simtrack_len==3',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_e>20 && gen_jet_pt<100 && abs(gen_jet_eta)>1.3 && abs(gen_jet_eta)<3 && simtrack_len==3')
