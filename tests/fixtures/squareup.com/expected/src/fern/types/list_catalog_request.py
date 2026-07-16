

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListCatalogRequest(UniversalBaseModel):
    """ """

    catalog_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The specific version of the catalog objects to be included in the response. 
    This allows you to retrieve historical
    versions of objects. The specified version value is matched against
    the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s' `version` attribute.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor returned in the previous response. Leave unset for an initial request.
    The page size is currently set to be 100.
    See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
    """

    types: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional case-insensitive, comma-separated list of object types to retrieve.
    
    The valid values are defined in the [CatalogObjectType](https://developer.squareup.com/reference/square_2021-08-18/enums/CatalogObjectType) enum, including
    `ITEM`, `ITEM_VARIATION`, `CATEGORY`, `DISCOUNT`, `TAX`,
    `MODIFIER`, `MODIFIER_LIST`, or `IMAGE`.
    
    If this is unspecified, the operation returns objects of all the types at the version of the Square API used to make the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
