import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--dir', default=None,
  help='Data files containing direcory')
parser.add_argument('--inFNRoots', default=None,
  help='Name roots for data files')
parser.add_argument('--extension', default=None,
  help='Only files with this extension will be considered')

parser.add_argument('--moments', default=0, type=int,
  help='Number of moments to be computed')

parser.add_argument('--histogram', action='store_true', default=False,
  help='Make histogram')
parser.add_argument('--xmin', default=0, type=float,
  help='Minimum x value for histograms')
parser.add_argument('--xmax', default=1000, type=float,
  help='Maximum x value for histograms')
parser.add_argument('--nbins', default=10, type=int,
  help='Number of bins for histograms')

parser.add_argument('--makeplots', action='store_true', default=False,
  help='Make data and histogram plots')

args = parser.parse_args()

