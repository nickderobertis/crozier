

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .marimo_dataframe_search_input_sort_item import MarimoDataframeSearchInputSortItem


class MarimoDataframeSearchInput(UniversalBaseModel):
    sort: typing.Optional[typing.List[MarimoDataframeSearchInputSortItem]] = None
    query: typing.Optional[str] = None
    filters: typing.Optional["MarimoDataframeSearchInputDefSchema0"] = None
    page_number: float
    page_size: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .marimo_dataframe_search_input_def_schema0 import MarimoDataframeSearchInputDefSchema0
from .marimo_dataframe_search_input_def_schema0children_item import MarimoDataframeSearchInputDefSchema0ChildrenItem

update_forward_refs(
    MarimoDataframeSearchInput,
    MarimoDataframeSearchInputDefSchema0=MarimoDataframeSearchInputDefSchema0,
    MarimoDataframeSearchInputDefSchema0ChildrenItem=MarimoDataframeSearchInputDefSchema0ChildrenItem,
)
