

import typing

from .patch_item import PatchItem

Patch = typing.List[PatchItem]
"""
A set of changes described in JSON Patch format: http://jsonpatch.com/ (RFC 6902)
"""
