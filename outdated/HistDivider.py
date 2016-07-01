from ROOT import TCanvas, gDirectory

#need develloppement about hist limits & maybe rename

def histdivider(tree, title, var, cut1, cut2):
    """
    returns a histogram of the two histograms associated with the two 
    variables with their own cut
    the returned hist will be hist1/hist2
    """
    tree.Project('hist{t}'.format(t=title), var, cut1)
    tree.Project('tmphist{t}'.format(t=title), var, cut2)
    divided_hist = gDirectory.Get('hist{t}'.format(t=title))
    divided_hist.Divide(gDirectory.Get('tmphist{t}'.format(t=title)))
    divided_hist.SetTitle(title)
    divided_hist.SetStats(False)
    return divided_hist
