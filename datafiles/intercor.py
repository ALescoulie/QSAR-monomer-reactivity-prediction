import os
import numpy as np
import matplotlib.pyplot as plt
import argparse
import scipy.stats as sp

def open_txt(filename):
    datafile = os.path.join(filename)
    outfile = open(datafile, "r")
    data = outfile.readlines()

    # Extracting lables
    lab = []

    for line in data:
        if "NAME" in line:
            lab = line
            lab = lab.split()
            lab = lab[2:]
    
    # Isolating descriptors
    des = np.genfromtxt(data, delimiter="\t")
    des = des[1:,2:]
    dim = des.shape[1]
    return lab, dim, des

def corrcoef(x, y):
    corrvec = sp.stats.pearsonr(x,y)
    r_squared = corrvec[0]
    return r_squared

def drawtab(arr, lab, name):
    CORRtab = plt.table(cellText=arr, rowLabels=lab, colLabels=lab)
    CORRtab.scale(16,16)
    CORRtab.auto_set_font_size(False)
    CORRtab.set_fontsize(32)
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
    for pos in ['right','top','bottom','left']:
        plt.gca().spines[pos].set_visible(False)
    plt.savefig(name, bbox_inches='tight', pad_inches=0.05)
    return

if __name__ == "__main__":
    
    ##getting arguments
    parser = argparse.ArgumentParser(description="This script analyzes the correlation between descriptors from exported Dragon 7 tab delinated text files.")
    parser.add_argument("txt_file", help="filepath of the dragon exported descriptors")
    args = parser.parse_args()
    
    # Opening file
    labels, ydim, DESC = open_txt(args.txt_file)
    
    # Caculating intercorrlation
    CORR = np.zeros((ydim, ydim))
    
    for n in range(0, ydim):
        for m in range(0, ydim):
            xvar = DESC[:,m]
            yvar = DESC[:,n]
            CORR[m,n] = corrcoef(xvar, yvar)
            if m == ydim:
                xvar = DESC[:, ydim]
                yvar = DESC[:, n]
                CORR[m,n] = corrcoef(xvar, yvar)
                if n == ydim:
                    for m in range(0, ydim):
                        n = ydim
                        xvar = DESC[:,ydim]
                        yvar = DESC[:,n]
                        CORR[m,n] = corrcoef(xvar,yvar)

    # Rounding r^2 values
    CORR = np.around(CORR, 3)
    
    # Complete table
    drawtab(CORR, labels, 'Correlation_table.png')
    
    # Removing high correlation values
    for n in range(0, ydim):
        for m in range(0, ydim):
            if abs(CORR[m,n]) >= 0.3:
                CORR[m,n] = 0
    
    # Ammended table
    drawtab(CORR, labels, 'Low_correlation_table.png')
