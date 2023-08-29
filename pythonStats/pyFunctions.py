from tkinter import Scale
import scipy.stats as stats 
import numpy as npy #has : 
    #npy.mean (mean) 
    #npy.std (standard deviation) 
    #npy.var (variance) 
    #npy.sem (standard error)
    #stats.norm.interval (CI for mean) parameters: confidence = (confidence), loc = (mean), scale = (standard error)
    #note : standard error formula : std/m.sqrt(n)

import math as m

ROUND = 4   #decimal place to round, default 4, can make whatever
POSITION = "th"
match ROUND%10:
    case 1:
        POSITION = "st"
    case 2:
        POSITION = "nd"
    case 3:
        POSITION = "rd"
    


#TESTS ---------------------------

def MTest1sRaw(data, comparison, popMean=0, alpha=0.05) :
    MTest1SData(npy.mean(data), comparison, popMean, npy.std(data), len(data), alpha)
    #print(stats.ttest_1samp(a = data, popmean = popMean, alternative= comp))

def MTest1SData(Smean, std, comparison, popMean, n, alpha):
    SE = std/m.sqrt(n)
    tStat = (Smean-popMean)/SE
    pVal = stats.t.cdf(tStat, n-1)
    sign = "!="
    
    print("---------------------")
    if comparison== "less" or comparison == "<":
        sign = "<"
    elif comparison == "greater" or comparison == ">":
        pVal = 1- pVal
        sign = ">"
    elif comparison == "not equal" or comparison == "!=": 
        pVal = 2*min(pVal, 1-pVal)
        sign = "!="
    else:
        print("|   No parameter or wrong comparison. Assumed \"not equal\"\n|   Acceptable inputs: \"less\", \"greater\", or \"not equal\".\n|   ")
        pVal = 2*min(pVal, 1-pVal)
        sign = "!="
    
    pVal = round(pVal, ROUND)
    tStat = round(tStat, ROUND)
    SE = round(SE, ROUND)
    
    
    print("|   1 SAMPLE T TEST\n|   Rounded to the {0}{1} decimal.\n|   \t H0:\tmu = {2}\n|   \t Ha:\tmu {3} {2}".format(ROUND, POSITION, popMean, sign))
    print("| standard error:\t{}\n|    t-statistic:\t{}\n|        p-value:\t{}".format(SE, tStat, pVal))

    if (pVal<alpha):
        print("|   We reject the null because the p-value of {} is less than a = {}.\n|   Therefore, we have convincing evidence that...".format(pVal, alpha))
    else:
        print("|   We fail to reject the null because the p-value of {} is greater than a = {}.\n|   Therefore, we have do not have convincing evidence that...".format(pVal, alpha))
    print("---------------------\n")
            

def MTest2SampleData(Smean1, std1, n1, comparison, Smean2, std2, n2, alpha=0.05):
    SE = m.sqrt(pow(std1, 2)/n1+pow(std2, 2)/n2)
    tStat = (Smean1-Smean2)/SE
    df = (pow(pow(std1,2)/n1 + pow(std2,2)/n2 ,2))/((1/(n1-1))*(pow(std1,2)/n1)+(1/(n2-1))*(pow(std2,2)/n2))
    print(df)
    pVal = stats.t.cdf(tStat, n1+n2-2)
    sign = "!="

    print("---------------------")
    if comparison== "less" or comparison == "<":
        sign = "<"
    elif comparison == "greater" or comparison == ">":
        pVal = 1- pVal
        sign = ">"
    elif comparison == "not equal" or comparison == "!=": 
        pVal = 2*min(pVal, 1-pVal)
        sign = "!="
    else:
        print("|   No parameter or wrong comparison. Assumed \"not equal\"\n|   Acceptable inputs: \"less\", \"greater\", or \"not equal\".\n|   ")
        pVal = 2*(1-pVal)
        sign = "!="
    
    pVal = round(pVal, ROUND)
    tStat = round(tStat, ROUND)
    SE = round(SE, ROUND)
    
    print("|   2 SAMPLE T TEST\n|   Rounded to the {}{} decimal.\n|   \t H0:\tmu1 = mu2\n|   \t Ha:\tmu1 {} mu2".format(ROUND, POSITION, sign))
    print("| standard error:\t{}\n|    t-statistic:\t{}\n|        p-value:\t{}".format(SE, tStat, pVal))





#---------------------------------


#INTERVALS -----------------------

def MIntervalRaw(data, confidence) :
    MIntervalData(npy.mean(data), npy.std(data), len(data), confidence)

def MIntervalData(Smean, std, n, confidence):
    #ME = stats.t.ppf(confidence/2, n-1 ) #ppf -> inverse cdf (cumulative density function )
    lBound, uBound = stats.norm.interval(confidence = confidence, loc = Smean, scale = std/m.sqrt(n)) # steps :
    # stats.norm.interval , returns a tuple
    # assigns to lBound and uBound
    
    print("---------------------")
    print("|   We are {}% confident that the the true mean is between {} and {}.".format(int(100*confidence), round(lBound, ROUND), round(uBound, ROUND)))
    print("---------------------\n")

def VIntervalRaw(data, confidence) :
    VIntervalData(npy.var(data), len(data)-1, confidence)

def VIntervalData(Svar, df, confidence):
    lBound = (df*Svar)/stats.chi2.ppf(1-(1-confidence)/2, df)
    uBound = (df*Svar)/stats.chi2.ppf(((1-confidence)/2), df)
    print("---------------------")
    print("|   We are {}% confident that the true variance is between {} and {}.".format( int(100*confidence), round(lBound,ROUND), round(uBound,ROUND)))
    print("---------------------\n")

#----------------------------------

#OTHER FUNCTIONS ---------------

#def compare(altComparison):
    
    
    #match altComparison:
    #    case "less":
    #        return altComparison
    #    case "more":
    #        return "greater"
    #    case "not equal":
    #        return "two-sided"
    #    case _:
    #        print("No parameter or wrong comparison. Assigned to \"not equal\"\n Acceptable inputs: \"less\", \"greater\", or \"not equal\".")
    #        return;



#---------------------
  
VIntervalRaw([85,90,94,89,90,93,95,96,92,93,93,95], 0.95) # (4.4711, 25.6849)
MIntervalRaw([85,90,94,89,90,93,95,96,92,93,93,95], 0.95) # (90.3945, 93.7722)
#MTest1sRaw([23,24,32,12,32,32,43,23,21,32,43,23,43,33,24,43,23,43,23,32], "dfsf", 32)
MTest1SData(Smean = 44.9, comparison="!=", popMean=40, std=8.9,n=15,alpha =0.05) # (H0: mu = 40, HA: mu != 40,t: 2.1323, p: 0.0512, FTR)
MTest2SampleData(300,18.5,40,"!=",305,16.7,38, 0.05)

