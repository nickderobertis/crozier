

import typing

from .access_rights import AccessRights

AccessGrants = typing.Dict[str, AccessRights]
"""
A map from each principal to its rights.

The map can have at most 1,000 entries and 65,536 bytes of principal IDs, and no entry has an
empty set of rights. Decoding rejects a repeated principal.
"""
