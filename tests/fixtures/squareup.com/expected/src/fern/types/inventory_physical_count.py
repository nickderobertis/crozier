

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .source_application import SourceApplication


class InventoryPhysicalCount(UniversalBaseModel):
    """
    Represents the quantity of an item variation that is physically present
    at a specific location, verified by a seller or a seller's employee. For example,
    a physical count might come from an employee counting the item variations on
    hand or from syncing with an external system.
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

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    An RFC 3339-formatted timestamp that indicates when the physical count is received.
    """

    employee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-generated ID of the [Employee](https://developer.squareup.com/reference/square_2021-08-18/objects/Employee) responsible for the
    physical count.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique Square-generated ID for the
    [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount).
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-generated ID of the [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) where the related
    quantity of items is being tracked.
    """

    occurred_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A client-generated RFC 3339-formatted timestamp that indicates when
    the physical count was examined. For physical count updates, the `occurred_at`
    timestamp cannot be older than 24 hours or in the future relative to the
    time of the request.
    """

    quantity: typing.Optional[str] = pydantic.Field(default=None)
    """
    The number of items affected by the physical count as a decimal string.
    The number can support up to 5 digits after the decimal point.
    """

    reference_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional ID provided by the application to tie the
    [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to an external
    system.
    """

    source: typing.Optional[SourceApplication] = None
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
