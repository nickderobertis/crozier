

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .error import Error


class SearchCatalogItemsResponse(UniversalBaseModel):
    """
    Defines the response body returned from the [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items) endpoint.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Pagination token used in the next request to return more of the search result.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    items: typing.Optional[typing.List["CatalogObject"]] = pydantic.Field(default=None)
    """
    Returned items matching the specified query expressions.
    """

    matched_variation_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Ids of returned item variations matching the specified query expression.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .catalog_object import CatalogObject

update_forward_refs(SearchCatalogItemsResponse)
