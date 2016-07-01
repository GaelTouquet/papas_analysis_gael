from ROOT import TFile, TH1F
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator
import tdrstyle

fil = TFile('./rootfiles/neutral_hadron_tree.root')
tree = fil.Get('events')

relcomp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3 && cmsjet_e>0',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3 && papasjet_e>0')

fil2 = TFile('./rootfiles/neutral_hadron_cmsjet_tree.root')
tree2 = fil2.Get('events')
test = TH1F('test', 'test', 100, 0, 3)
tree2.Project('test', 'jet1_rec_e/jet1_e', 'jet1_pt>1 && jet1_pt<10 && abs(jet1_eta)<1.3 && jet1_rec_e>0')
cms_style2.formatHisto(test)
test.Draw('hist same')
relcomp.legend.AddEntry(test, 'cms_jet', 'lp')

relcompb = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3 && cmsjet_e>0 && gen_jet_pt>3 && cmsjet_pt>5',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3 && papasjet_e>0 && gen_jet_pt>3 && papasjet_pt>5')

fil2b = TFile('./rootfiles/neutral_hadron_cmsjet_tree.root')
tree2b = fil2.Get('events')
testb = TH1F('testb', 'testb', 100, 0, 3)
tree2b.Project('testb', 'jet1_rec_e/jet1_e', 'jet1_pt>1 && jet1_pt<10 && abs(jet1_eta)<1.3 && jet1_rec_e>0')
cms_style2.formatHisto(testb)
testb.Draw('hist same')
relcompb.legend.AddEntry(test, 'cms_jet', 'lp')

relcomp2 = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3 && simtrack_len<5',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3 && simtrack_len<5')

relcomp1 = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = 0, xmax = 3, xvar = 'E_{rec}/E_{gen}',
                      var1 = 'cmsjet_e/gen_jet_e', 
                      cut1 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3 && simtrack_len>8',
                      var2 = 'papasjet_e/gen_jet_e',
                      cut2 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3 && simtrack_len>8')

abscomp = HistComparator(tree, style1 = cms_style, style2 = papas_style,
                      nbin = 100, xmin = -20, xmax = 20, xvar = 'E_{rec}-E_{gen}',
                      var1 = 'cmsjet_e-gen_jet_e', 
                      cut1 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3',
                      var2 = 'papasjet_e-gen_jet_e',
                      cut2 = 'gen_jet_pt>1 && gen_jet_pt<10 && abs(gen_jet_eta)<1.3')
