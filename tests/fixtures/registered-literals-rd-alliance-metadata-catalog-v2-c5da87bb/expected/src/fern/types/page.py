

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Page(UniversalBaseModel):
    items_per_page: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemsPerPage"),
        pydantic.Field(alias="itemsPerPage", description="Number of items per page of results."),
    ] = None
    """
    Number of items per page of results.
    """

    current_item_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentItemCount"),
        pydantic.Field(alias="currentItemCount", description="Number of items in the current page of results."),
    ] = None
    """
    Number of items in the current page of results.
    """

    start_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="startIndex"),
        pydantic.Field(
            alias="startIndex",
            description="Index of the first item in the current page of results. Items are counted from 1.",
        ),
    ] = None
    """
    Index of the first item in the current page of results. Items are counted from 1.
    """

    total_items: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalItems"),
        pydantic.Field(
            alias="totalItems",
            description="Total number of items in the result set (equal to the index of the last item).",
        ),
    ] = None
    """
    Total number of items in the result set (equal to the index of the last item).
    """

    page_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="pageIndex"),
        pydantic.Field(
            alias="pageIndex", description="Index of the current page of results. Pages are counted from 1."
        ),
    ] = None
    """
    Index of the current page of results. Pages are counted from 1.
    """

    total_pages: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalPages"),
        pydantic.Field(alias="totalPages", description="Total number of pages in the result"),
    ] = None
    """
    Total number of pages in the result
    """

    next_link: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextLink"),
        pydantic.Field(alias="nextLink", description="URL from which to obtain the next page of results."),
    ] = None
    """
    URL from which to obtain the next page of results.
    """

    previous_link: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="previousLink"),
        pydantic.Field(alias="previousLink", description="URL from which to obtain the previous page of results."),
    ] = None
    """
    URL from which to obtain the previous page of results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
