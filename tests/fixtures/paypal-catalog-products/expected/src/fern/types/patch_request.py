

import typing

from .patch import Patch

PatchRequest = typing.List[Patch]
"""
An array of JSON patch objects to apply partial updates to resources.
"""
