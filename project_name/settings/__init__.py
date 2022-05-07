"""
Django settings for project_name project.

Default settings set to local.
"""

try:
    from .local import *
except ImportError:
    pass
