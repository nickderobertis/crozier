

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InventoryCount(UniversalBaseModel):
    """
    Represents Square-estimated quantity of items in a particular state at a
    particular seller location based on the known history of physical counts and
    inventory adjustments.
    """

    calculated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    An RFC 3339-formatted timestamp that indicates when the most recent physical count or adjustment affecting
    the estimated count is received.
    """

    catalog_object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-generated ID of the
    [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) being tracked.
    """

    catalog_object_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [type](https://developer.squareup.com/reference/square_2021-08-18/enums/CatalogObjectType) of the
    [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) being tracked. Tracking is only
    supported for the `ITEM_VARIATION` type.
    """

    is_estimated: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the inventory count is for composed variation (TRUE) or not (FALSE). If true, the inventory count will not be present in the response of
    any of these endpoints: [BatchChangeInventory](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-change-inventory), 
    [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-changes), 
    [BatchRetrieveInventoryCounts](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-counts), and 
    [RetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/retrieve-inventory-changes).
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-generated ID of the [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) where the related
    quantity of items is being tracked.
    """

    quantity: typing.Optional[str] = pydantic.Field(default=None)
    """
    The number of items affected by the estimated count as a decimal string.
    Can support up to 5 digits after the decimal point.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current [inventory state](https://developer.squareup.com/reference/square_2021-08-18/enums/InventoryState) for the related
    quantity of items.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
