

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_union_one import NestedUnionOne
from .outer_union import OuterUnion


class TaggedUnionContainer(UniversalBaseModel):
    direct: NestedUnionOne
    nested: OuterUnion

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
