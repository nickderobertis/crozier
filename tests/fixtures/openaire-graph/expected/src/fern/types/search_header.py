

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_header_debug import SearchHeaderDebug


class SearchHeader(UniversalBaseModel):
    debug: typing.Optional[SearchHeaderDebug] = None
    num_found: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numFound"), pydantic.Field(alias="numFound")
    ] = None
    max_score: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxScore"), pydantic.Field(alias="maxScore")
    ] = None
    query_time: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="queryTime"), pydantic.Field(alias="queryTime")
    ] = None
    page: typing.Optional[int] = None
    page_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")
    ] = None
    total_pages: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalPages"), pydantic.Field(alias="totalPages")
    ] = None
    total_links: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalLinks"), pydantic.Field(alias="totalLinks")
    ] = None
    next_cursor: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextCursor"),
        pydantic.Field(
            alias="nextCursor",
            description="nextCursor - to be used in the next request to get the next page of results. \nYou can repeat this process until you’ve fetched as many results as you want, \nor until the nextCursor returned matches the current cursor you’ve already specified, \nindicating that there are no more results.",
        ),
    ] = None
    """
    nextCursor - to be used in the next request to get the next page of results. 
    You can repeat this process until you’ve fetched as many results as you want, 
    or until the nextCursor returned matches the current cursor you’ve already specified, 
    indicating that there are no more results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
