

import typing

from .nested_union_one import NestedUnionOne

OuterUnion = typing.Union[NestedUnionOne, bool]
