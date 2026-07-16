

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogIdMapping(UniversalBaseModel):
    """
    A mapping between a temporary client-supplied ID and a permanent server-generated ID.

    When calling [UpsertCatalogObject](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/upsert-catalog-object) or
    [BatchUpsertCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/batch-upsert-catalog-objects) to
    create a [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) instance, you can supply
    a temporary ID for the to-be-created object, especially when the object is to be referenced
    elsewhere in the same request body. This temporary ID can be any string unique within
    the call, but must be prefixed by "#".

    After the request is submitted and the object created, a permanent server-generated ID is assigned
    to the new object. The permanent ID is unique across the Square catalog.
    """

    client_object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The client-supplied temporary `#`-prefixed ID for a new `CatalogObject`.
    """

    object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The permanent ID for the CatalogObject created by the server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
