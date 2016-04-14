from ROOT import TFile
from papas_analysis_gael.tools.style import papas_style, cms_style
from papas_analysis_gael.tools.HistHandler import HistHandler

cms_file = TFile('./rootfiles/Coneanalysis.root')

cms = cms_file.Get('ptcs')

hist = HistHandler(cms, cms_style,
                   var = 'particle_pdgid',
                   cut = 'is_gen_matched==0',
                   xmin = -250, xmax = 250, nbin = 100,
                   xvar = 'pdgid')

hist2 = HistHandler(cms, papas_style,
                    var = 'particle_pdgid',
                    cut = 'is_gen_matched==1',
                    xmin = -250, xmax = 250, nbin = 100,
                    xvar = 'pdgid')

hist.Draw()
hist.canvas[0].SetLogy()
hist2.Draw()
hist2.canvas[0].SetLogy()
hist.change(var = 'particle_e', xvar = 'E(GeV)', xmin = 0, xmax = 30, log = True)
hist2.change(var = 'particle_e', xvar = 'E(GeV)', xmin = 0, xmax = 4000, log = True)
hist.change(cutadd = 'particle_pdgid==22', xvar = 'E(GeV)', xmin = 0, xmax = 5, log = True)
hist2.change(cutadd = 'particle_pdgid==22', xvar = 'E(GeV)', xmin = 0, xmax = 2000, log = True)
hist.change(cut = 'is_gen_matched==0 && particle_pdgid==130', xvar = 'E(GeV)', xmin = 0, xmax = 30, log = True)
hist2.change(cut = 'is_gen_matched==1 && particle_pdgid==130', xvar = 'E(GeV)', xmin = 0, xmax = 2500, log = True)
hist.change(cut = 'is_gen_matched==0 && abs(particle_pdgid)==211', xvar = 'E(GeV)', xmin = 0.55, xmax = 0.66, log = True)
hist2.change(cut = 'is_gen_matched==1 && abs(particle_pdgid)==211', xvar = 'E(GeV)', xmin = 0, xmax = 4000, log = True)
