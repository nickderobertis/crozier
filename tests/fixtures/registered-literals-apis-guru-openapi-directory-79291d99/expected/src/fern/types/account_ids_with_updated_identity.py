

import typing

from .identity_update_types import IdentityUpdateTypes

AccountIdsWithUpdatedIdentity = typing.Dict[str, typing.List[IdentityUpdateTypes]]
"""
An object with keys of `account_id`'s that are mapped to their respective identity attributes that changed.

Example: `{ "XMBvvyMGQ1UoLbKByoMqH3nXMj84ALSdE5B58": ["PHONES"] }`
"""
