

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .marimo_table_search_input_def_schema0operator import MarimoTableSearchInputDefSchema0Operator
from .marimo_table_search_input_def_schema0type import MarimoTableSearchInputDefSchema0Type


class MarimoTableSearchInputDefSchema0(UniversalBaseModel):
    type: typing.Optional[MarimoTableSearchInputDefSchema0Type] = None
    operator: typing.Optional[MarimoTableSearchInputDefSchema0Operator] = None
    children: typing.Optional[typing.List["MarimoTableSearchInputDefSchema0ChildrenItem"]] = None
    negate: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .marimo_table_search_input_def_schema0children_item import MarimoTableSearchInputDefSchema0ChildrenItem

update_forward_refs(
    MarimoTableSearchInputDefSchema0,
    MarimoTableSearchInputDefSchema0ChildrenItem=MarimoTableSearchInputDefSchema0ChildrenItem,
)
