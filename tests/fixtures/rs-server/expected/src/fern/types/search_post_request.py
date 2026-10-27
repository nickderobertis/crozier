

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .post_fields_extension import PostFieldsExtension
from .search_post_request_filter_lang import SearchPostRequestFilterLang
from .search_post_request_intersects import SearchPostRequestIntersects
from .sort_extension import SortExtension


class SearchPostRequest(UniversalBaseModel):
    collections: typing.Optional[typing.List[str]] = None
    ids: typing.Optional[typing.List[str]] = None
    bbox: typing.Optional[typing.List[typing.Any]] = None
    intersects: typing.Optional[SearchPostRequestIntersects] = None
    datetime: typing.Optional[str] = None
    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Limits the number of results that are included in each page of the response (capped to 10_000).
    """

    conf: typing.Optional[typing.Dict[str, typing.Any]] = None
    query: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = None
    sortby: typing.Optional[typing.List[SortExtension]] = pydantic.Field(default=None)
    """
    An array of property (field) names, and direction in form of '{'field': '<property_name>', 'direction':'<direction>'}'
    """

    fields: typing.Optional[PostFieldsExtension] = pydantic.Field(default=None)
    """
    Include or exclude fields from items body.
    """

    filter: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    A CQL filter expression for filtering items.
    """

    filter_crs: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="filter-crs"),
        pydantic.Field(
            alias="filter-crs",
            description="The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`",
        ),
    ] = None
    """
    The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`
    """

    filter_lang: typing_extensions.Annotated[
        typing.Optional[SearchPostRequestFilterLang],
        FieldMetadata(alias="filter-lang"),
        pydantic.Field(alias="filter-lang", description="The CQL filter encoding that the 'filter' value uses."),
    ] = None
    """
    The CQL filter encoding that the 'filter' value uses.
    """

    token: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(SearchPostRequest)
