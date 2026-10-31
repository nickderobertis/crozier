

import typing

from .access_right import AccessRight

AccessRights = typing.List[AccessRight]
"""
A set of rights.

The set is encoded as distinct right names in `read`, `history`, `write`, `create`, `remove`,
`share`, `manage`, `admin` order. Decoding accepts any order and rejects a repeated name.
"""
