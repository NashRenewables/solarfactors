# -*- coding: utf-8 -*-

from pvfactors.version import __version__  # noqa: F401
import logging
logging.basicConfig()

class PVFactorsError(Exception):
    pass

from . import _version
__version__ = _version.get_versions()['version']
