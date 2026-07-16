

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .error import Error


class BatchRetrieveCatalogObjectsResponse(UniversalBaseModel):
    """ """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    objects: typing.Optional[typing.List["CatalogObject"]] = pydantic.Field(default=None)
    """
    A list of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s returned.
    """

    related_objects: typing.Optional[typing.List["CatalogObject"]] = pydantic.Field(default=None)
    """
    A list of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s referenced by the object in the `objects` field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .catalog_object import CatalogObject

update_forward_refs(BatchRetrieveCatalogObjectsResponse)
