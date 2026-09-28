

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .marimo_dataframe_search_input_def_schema0operator import MarimoDataframeSearchInputDefSchema0Operator
from .marimo_dataframe_search_input_def_schema0type import MarimoDataframeSearchInputDefSchema0Type


class MarimoDataframeSearchInputDefSchema0(UniversalBaseModel):
    type: typing.Optional[MarimoDataframeSearchInputDefSchema0Type] = None
    operator: typing.Optional[MarimoDataframeSearchInputDefSchema0Operator] = None
    children: typing.Optional[typing.List["MarimoDataframeSearchInputDefSchema0ChildrenItem"]] = None
    negate: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .marimo_dataframe_search_input_def_schema0children_item import MarimoDataframeSearchInputDefSchema0ChildrenItem

update_forward_refs(
    MarimoDataframeSearchInputDefSchema0,
    MarimoDataframeSearchInputDefSchema0ChildrenItem=MarimoDataframeSearchInputDefSchema0ChildrenItem,
)
