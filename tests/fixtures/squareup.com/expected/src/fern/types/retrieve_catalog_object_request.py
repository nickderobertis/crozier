

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RetrieveCatalogObjectRequest(UniversalBaseModel):
    """ """

    catalog_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Requests objects as of a specific version of the catalog. This allows you to retrieve historical
    versions of objects. The value to retrieve a specific version of an object can be found
    in the version field of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s.
    """

    include_related_objects: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, the response will include additional objects that are related to the
    requested object, as follows:
    
    If the `object` field of the response contains a `CatalogItem`, its associated
    `CatalogCategory`, `CatalogTax`, `CatalogImage` and `CatalogModifierList` objects will
    be returned in the `related_objects` field of the response. If the `object` field of
    the response contains a `CatalogItemVariation`, its parent `CatalogItem` will be returned
    in the `related_objects` field of the response.
    
    Default value: `false`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
