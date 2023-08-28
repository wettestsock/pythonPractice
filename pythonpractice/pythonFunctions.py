import numpy as npy
import scipy.stats as stats



def FInterval(data, confidence) :
    df = len(data)-1
    var = npy.var(data)
    lBound = (df*var)/stats.chi2.ppf(1-(1-confidence)/2, df)
    uBound = (df*var)/stats.chi2.ppf(((1-confidence)/2), df)
    print("We are {}% confident that the true variance is between {} and {}.".format( int(100*confidence), round(lBound,4), round(uBound,4)))

FInterval([85,90,94,89,90,93,95,96,92,93,93,95], 0.95)