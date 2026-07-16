

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_measurement_unit import CatalogMeasurementUnit
from .inventory_adjustment import InventoryAdjustment
from .inventory_physical_count import InventoryPhysicalCount
from .inventory_transfer import InventoryTransfer


class InventoryChange(UniversalBaseModel):
    """
    Represents a single physical count, inventory, adjustment, or transfer
    that is part of the history of inventory changes for a particular
    [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) instance.
    """

    adjustment: typing.Optional[InventoryAdjustment] = None
    measurement_unit: typing.Optional[CatalogMeasurementUnit] = None
    measurement_unit_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the [CatalogMeasurementUnit](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogMeasurementUnit) object representing the catalog measurement unit associated with the inventory change.
    """

    physical_count: typing.Optional[InventoryPhysicalCount] = None
    transfer: typing.Optional[InventoryTransfer] = None
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates how the inventory change is applied. See
    [InventoryChangeType](https://developer.squareup.com/reference/square_2021-08-18/enums/InventoryChangeType) for all possible values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
