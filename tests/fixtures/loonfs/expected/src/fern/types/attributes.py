

import typing

from .attribute_value import AttributeValue

Attributes = typing.Dict[str, AttributeValue]
"""
A map from attribute keys to values, with at most 100 entries and 65,536 UTF-8 bytes of keys and
values in total.

Construction and decoding reject a map over these limits. An empty map means that the inode has
no attributes.
"""
