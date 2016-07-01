from ROOT import TFile
from HistEfficiency import HistEfficiency

cms_file = TFile('./rootfiles/cmssamplejetted.root')

cms_tree = cms_file.Get('events')

histeff = HistEfficiency(cms_tree,
                         


    var, cut, eff_cut,  
                                       xmin, xmax, nbin, 
                                       style1, varname, 
                                       efficiency_name,
                                       label1)
