# Copyright (c) 2017 National Research Foundation (South African Radio Astronomy Observatory)
# BSD license - see LICENSE for details

"""Root of the nosekatreport package."""

# BEGIN VERSION CHECK
# Get package version when locally imported from repo or via -e develop install
try:
    import katversion as _katversion
except ImportError:
    import time as _time

    __version__ = "0.0+unknown.{}".format(_time.strftime("%Y%m%d%H%M"))
else:
    __version__ = _katversion.get_version(__path__[0])
# END VERSION CHECK

from .plugin import *
from .decorators import *
