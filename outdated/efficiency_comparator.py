from ROOT import TFile, TCanvas
from HistDivider import histdivider
from cpyroot import *
import sys

def efficiency_hists(tree, t_var_cuts):
    hists = []
    for title, var, cut1, cut2 in t_var_cuts:
        hists.append(histdivider(tree, title, var, cut1, cut2))
    return hists

if __name__=='__main__':

    t_var_cuts = []
    t_var_cuts.append( ('efficiency : pt',
                        'jet1_pt',
                        'jet1_e>0 && jet1_rec_211_num==1',
                        'jet1_e>0') )
    t_var_cuts.append( ('efficiency : low pt',
                        'jet1_pt',
                        'jet1_e>0 && jet1_rec_211_num==1 && jet1_pt<3',
                        'jet1_e>0 && jet1_pt<3') )




    file1 = TFile('./rootfiles/{sample}.root'.format(sample=sys.argv[1]))
    file2 = TFile('./rootfiles/{sample}.root'.format(sample=sys.argv[2]))

    tree1 = file1.Get('events')
    tree2 = file2.Get('events')
    
    hists1 = efficiency_hists(tree1, t_var_cuts)
    hists2 = efficiency_hists(tree2, t_var_cuts)
    
    TCanvas()
    hists1[0].Draw()
    hists2[0].Draw('same')
    #hists2[1].Draw()
    

    #for i in range(len(t_var_cuts)):
    #    iter[2*i] = TCanvas()
    #    hists1[i].Draw()
    #    iter[2*i+1] = TCanvas()
    #    hists2[i].Draw()
 
        
