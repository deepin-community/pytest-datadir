from __future__ import absolute_import

try:
    from ._version import version
    __version__ = version
except ImportError:
    __version__ = version = 'unknown'
