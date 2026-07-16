

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .catalog_id_mapping import CatalogIdMapping
from .error import Error


class BatchUpsertCatalogObjectsResponse(UniversalBaseModel):
    """ """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    id_mappings: typing.Optional[typing.List[CatalogIdMapping]] = pydantic.Field(default=None)
    """
    The mapping between client and server IDs for this upsert.
    """

    objects: typing.Optional[typing.List["CatalogObject"]] = pydantic.Field(default=None)
    """
    The created successfully created CatalogObjects.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The database [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) of this update in RFC 3339 format, e.g., "2016-09-04T23:59:33.123Z".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .catalog_object import CatalogObject

update_forward_refs(BatchUpsertCatalogObjectsResponse)
