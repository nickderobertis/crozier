

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .marimo_table_search_input_sort_item import MarimoTableSearchInputSortItem


class MarimoTableSearchInput(UniversalBaseModel):
    sort: typing.Optional[typing.List[MarimoTableSearchInputSortItem]] = None
    query: typing.Optional[str] = None
    filters: typing.Optional["MarimoTableSearchInputDefSchema0"] = None
    page_number: float
    page_size: float
    max_columns: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .marimo_table_search_input_def_schema0 import MarimoTableSearchInputDefSchema0
from .marimo_table_search_input_def_schema0children_item import MarimoTableSearchInputDefSchema0ChildrenItem

update_forward_refs(
    MarimoTableSearchInput,
    MarimoTableSearchInputDefSchema0=MarimoTableSearchInputDefSchema0,
    MarimoTableSearchInputDefSchema0ChildrenItem=MarimoTableSearchInputDefSchema0ChildrenItem,
)
