

import typing

Labels = typing.Dict[str, str]
"""
Labels store metadata of an entity that can be used for filtering an entity list or for searching across entity types. 

Keys must be of length 1-63 characters, and cannot start with "kong", "konnect", "mesh", "kic", or "_".
"""
