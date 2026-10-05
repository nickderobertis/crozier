

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entry_node import EntryNode
from .entry_node_search_result_filters_item import EntryNodeSearchResultFiltersItem


class EntryNodeSearchResult(UniversalBaseModel):
    q: typing.Optional[str] = None
    node_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="nodeCount"), pydantic.Field(alias="nodeCount")
    ] = None
    page_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pageCount"), pydantic.Field(alias="pageCount")
    ] = None
    filters: typing.Optional[typing.List[EntryNodeSearchResultFiltersItem]] = None
    nodes: typing.Optional[typing.List[EntryNode]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
