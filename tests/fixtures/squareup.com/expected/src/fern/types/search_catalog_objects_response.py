

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .error import Error


class SearchCatalogObjectsResponse(UniversalBaseModel):
    """ """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to be used in a subsequent request. If unset, this is the final response.
    See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    latest_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    When the associated product catalog was last updated. Will
    match the value for `end_time` or `cursor` if either field is included in the `SearchCatalog` request.
    """

    objects: typing.Optional[typing.List["CatalogObject"]] = pydantic.Field(default=None)
    """
    The CatalogObjects returned.
    """

    related_objects: typing.Optional[typing.List["CatalogObject"]] = pydantic.Field(default=None)
    """
    A list of CatalogObjects referenced by the objects in the `objects` field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .catalog_object import CatalogObject

update_forward_refs(SearchCatalogObjectsResponse)
