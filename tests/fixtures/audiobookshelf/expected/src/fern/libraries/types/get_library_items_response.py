

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.collapse_series import CollapseSeries
from ...types.filter_by import FilterBy
from ...types.library_include import LibraryInclude
from ...types.library_item_base import LibraryItemBase
from ...types.limit import Limit
from ...types.media_type import MediaType
from ...types.minified import Minified
from ...types.page import Page
from ...types.sort_by import SortBy
from ...types.sort_desc import SortDesc
from ...types.total import Total


class GetLibraryItemsResponse(UniversalBaseModel):
    results: typing.Optional[typing.List[LibraryItemBase]] = None
    total: typing.Optional[Total] = None
    limit: typing.Optional[Limit] = None
    page: typing.Optional[Page] = None
    sort_by: typing_extensions.Annotated[
        typing.Optional[SortBy], FieldMetadata(alias="sortBy"), pydantic.Field(alias="sortBy")
    ] = None
    sort_desc: typing_extensions.Annotated[
        typing.Optional[SortDesc], FieldMetadata(alias="sortDesc"), pydantic.Field(alias="sortDesc")
    ] = None
    filter_by: typing_extensions.Annotated[
        typing.Optional[FilterBy], FieldMetadata(alias="filterBy"), pydantic.Field(alias="filterBy")
    ] = None
    media_type: typing_extensions.Annotated[
        typing.Optional[MediaType], FieldMetadata(alias="mediaType"), pydantic.Field(alias="mediaType")
    ] = None
    minified: typing.Optional[Minified] = None
    collapse_series: typing_extensions.Annotated[
        typing.Optional[CollapseSeries], FieldMetadata(alias="collapseSeries"), pydantic.Field(alias="collapseSeries")
    ] = None
    include: typing.Optional[LibraryInclude] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
