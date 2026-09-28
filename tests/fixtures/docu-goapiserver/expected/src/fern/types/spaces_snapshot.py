

import typing

from .space_snapshot import SpaceSnapshot

SpacesSnapshot = typing.Dict[str, typing.Dict[str, typing.Dict[str, SpaceSnapshot]]]
"""
Nested map keyed by school name, then room name, then period. Each leaf is a SpaceSnapshot. An empty result is {}.
"""
