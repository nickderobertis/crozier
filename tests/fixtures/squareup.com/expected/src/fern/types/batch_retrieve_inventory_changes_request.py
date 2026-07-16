

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BatchRetrieveInventoryChangesRequest(UniversalBaseModel):
    """ """

    catalog_object_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The filter to return results by `CatalogObject` ID.
    The filter is only applicable when set. The default value is null.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by a previous call to this endpoint.
    Provide this to retrieve the next set of results for the original query.
    
    See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    """

    location_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The filter to return results by `Location` ID. 
    The filter is only applicable when set. The default value is null.
    """

    states: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The filter to return `ADJUSTMENT` query results by
    `InventoryState`. This filter is only applied when set.
    The default value is null.
    """

    types: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The filter to return results by `InventoryChangeType` values other than `TRANSFER`.
    The default value is `[PHYSICAL_COUNT, ADJUSTMENT]`.
    """

    updated_after: typing.Optional[str] = pydantic.Field(default=None)
    """
    The filter to return results with their `calculated_at` value  
    after the given time as specified in an RFC 3339 timestamp. 
    The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    """

    updated_before: typing.Optional[str] = pydantic.Field(default=None)
    """
    The filter to return results with their `created_at` or `calculated_at` value  
    strictly before the given time as specified in an RFC 3339 timestamp. 
    The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
