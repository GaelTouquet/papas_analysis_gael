def xrootd(fname):
    return '/'.join( ['root://lyogrid06.in2p3.fr//dpm/in2p3.fr/home/cms/data',
                      fname] )

if __name__ == '__main__':
    import sys 
    print xrootd(sys.argv[1])
