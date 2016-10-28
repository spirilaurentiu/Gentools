# Load options definitions
execfile("genstatargs.py")

import glob
import re
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

rooti = 0
ix = 0
means = []
vars = []
if type(args.inFNRoots) is list:
  inFNRoots = args.inFNRoots
else:
  inFNRoots = [args.inFNRoots]
for inFNRoot in inFNRoots:
  if args.extension:
    FNlist = glob.glob(os.path.join(args.dir, inFNRoot + '*' + args.extension))
  else:
    FNlist = glob.glob(os.path.join(args.dir, inFNRoot + '*'))

  for FN in FNlist:
    fi = 0 # file index
    # Load data
    print 'Loading data from ' + FN + ' ... ',
    data = []
    with open(FN, 'r') as inFN:
      for line in inFN:
        words = re.sub(r'[.!,;?]', ' ', line).split()
        if len(words)>1:
          if words[0] == "acc": # insert conditions here
           data.append(float(words[1]) / 20.0) # process data here
    data = np.array(data)
    print 'Done.'
 
    # Moments
    if args.moments:
      means.append(np.mean(data))
      vars.append(np.var(data))
      print "File moments %.10lf %.10lf" % (means[ix], vars[ix])

    # Histogram
    if args.histogram:
      hist = np.histogram(data, bins=args.nbins, range=(args.xmin, args.xmax))
      print "File histogram"
      for i in range(args.nbins):
        print hist[1][i] + (hist[1][i+1] - hist[1][i])/2, hist[0][i]

    # Plot 
    if args.makeplots:
      ax = plt.subplot(1, 2, rooti + 1)
      figFN = 'temp.' + str(ix)  + 'pdf'
      plt.plot(data)
      plt.savefig(figFN, format='pdf', dpi=600)

    ix = ix + 1
    fi = fi + 1
  ## End of file list
  # Analysis per root
  rooti = rooti + 1

totmean = np.mean(means)
varmean = np.var(means)
stdmean = np.std(means)
print "Final moments mean %.10lf var %.10lf stdev %.10lf " % (totmean, varmean, stdmean)
