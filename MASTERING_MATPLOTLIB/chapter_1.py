import matplotlib
matplotlib.use("nbagg")
%matplotlib inline


from glob import glob
from modulefinder import Module
from modulefinder import ModuleFinder
from os.path import dirname
from pprint import pprint
import sys
import trace
import urllib.request

import matplotlib.pyplot as plt
from IPython.core.display import Image

from pycallgraph import Config
from pycallgraph import GlobbingFilter
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

sys.path.append("../lib")
from architecture.modarch import matplotlib_groupings
import modfind
import modgraph
from modutil import ls, rm
