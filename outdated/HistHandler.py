from ROOT import TCanvas, gDirectory, TH1F
from cpyroot.tools.histcomparator import HistComparator

class HistHandler(object):
    
    def __init__(self, tree, hist_carac_list = []):
        """
        argument hist_carac_list must be a list of dictionnaries each having 
        title, var and cut argument
        """
        self.tree = tree
        self.hists = {}
        for hist in hist_carac_list:
            title = hist['title']
            self.tree.Project(title, hist['var'], hist['cut'])
            self.hists[title] = gDirectory.Get(title)
        self.canvas = {}
        self.comparators = {}
        self.compared_trees = {}
        
        
    def create_hist(self, treetitle, title, var, cut, show=False):
        self.tree.Project(title, var, cut)
        self.hists[title] = gDirectory.Get(title)
        if show:
            self.show_hist(title)

    def set_style(self, title, style, show=False):
        style.formatHisto(self.hists[title])
        if show:
            self.show_hist(title)
        
    def compare_trees(self, title, compared_tree, var, cut, show=False):
        comp_histname = 'compared_{n}'.format(n=compared_tree.GetName())
        while comp_histname in self.compared_trees:
            comp_histname += 'bis'
        compared_tree.Project(comp_histname, var, cut)
        compared_hist = gDirectory.Get(comp_histname)
        self.create_hist(title, var, cut)
        self.comparators[title] = HistComparator(var,
                                                 self.hists[title],
                                                 compared_hist,
                                                 self.hists[title].GetName(),
                                                 comp_histname)
        if show:
            self.comparators[title].draw()
                     

    def hist_compare(self, title, title1, title2, var, cut1, cut2, show=False):
        self.create_hist(title1, var, cut1)
        self.create_hist(title2, var, cut2)
        self.comparators[title] = HistComparator(var, 
                                                 self.hists[title1], 
                                                 self.hists[title2],
                                                 title1, title2)
        self.hists[title] = self.comparators[title].ratio
        self.hists[title].SetTitle(title)
        if show:
            self.comparators[title].draw()
            

    def show_hist(self, title):
        self.canvas[title] = TCanvas()
        self.hists[title].Draw()

