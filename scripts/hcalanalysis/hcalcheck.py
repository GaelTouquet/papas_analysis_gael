from ROOT import TFile
from papas_analysis_gael.tools.style import papas_style, cms_style, cms_style2, papas_style2
from papas_analysis_gael.tools.HistComparator import HistComparator

fil = TFile('./rootfiles/neutral_hadron_cmsjet_tree.root')
tree = fil.Get('events')

