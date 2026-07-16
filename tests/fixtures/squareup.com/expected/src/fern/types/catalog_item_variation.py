

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_item_option_value_for_item_variation import CatalogItemOptionValueForItemVariation
from .catalog_stock_conversion import CatalogStockConversion
from .item_variation_location_overrides import ItemVariationLocationOverrides
from .money import Money


class CatalogItemVariation(UniversalBaseModel):
    """
    An item variation (i.e., product) in the Catalog object model. Each item
    may have a maximum of 250 item variations.
    """

    available_for_booking: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If the `CatalogItem` that owns this item variation is of type
    `APPOINTMENTS_SERVICE`, a bool representing whether this service is available for booking.
    """

    inventory_alert_threshold: typing.Optional[int] = pydantic.Field(default=None)
    """
    If the inventory quantity for the variation is less than or equal to this value and `inventory_alert_type`
    is `LOW_QUANTITY`, the variation displays an alert in the merchant dashboard.
    
    This value is always an integer.
    """

    inventory_alert_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates whether the item variation displays an alert when its inventory quantity is less than or equal
    to its `inventory_alert_threshold`.
    """

    item_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the `CatalogItem` associated with this item variation.
    """

    item_option_values: typing.Optional[typing.List[CatalogItemOptionValueForItemVariation]] = pydantic.Field(
        default=None
    )
    """
    List of item option values associated with this item variation. Listed
    in the same order as the item options of the parent item.
    """

    location_overrides: typing.Optional[typing.List[ItemVariationLocationOverrides]] = pydantic.Field(default=None)
    """
    Per-location price and inventory overrides.
    """

    measurement_unit_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the ‘CatalogMeasurementUnit’ that is used to measure the quantity
    sold of this item variation. If left unset, the item will be sold in
    whole quantities.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The item variation's name. This is a searchable attribute for use in applicable query filters, and its value length is of Unicode code points.
    """

    ordinal: typing.Optional[int] = pydantic.Field(default=None)
    """
    The order in which this item variation should be displayed. This value is read-only. On writes, the ordinal
    for each item variation within a parent `CatalogItem` is set according to the item variations's
    position. On reads, the value is not guaranteed to be sequential or unique.
    """

    price_money: typing.Optional[Money] = None
    pricing_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates whether the item variation's price is fixed or determined at the time
    of sale.
    """

    service_duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    If the `CatalogItem` that owns this item variation is of type
    `APPOINTMENTS_SERVICE`, then this is the duration of the service in milliseconds. For
    example, a 30 minute appointment would have the value `1800000`, which is equal to
    30 (minutes) * 60 (seconds per minute) * 1000 (milliseconds per second).
    """

    sku: typing.Optional[str] = pydantic.Field(default=None)
    """
    The item variation's SKU, if any. This is a searchable attribute for use in applicable query filters.
    """

    stockable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether stock is counted directly on this variation (TRUE) or only on its components (FALSE).
    For backward compatibility missing values will be interpreted as TRUE.
    """

    stockable_conversion: typing.Optional[CatalogStockConversion] = None
    team_member_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tokens of employees that can perform the service represented by this variation. Only valid for
    variations of type `APPOINTMENTS_SERVICE`.
    """

    track_inventory: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, inventory tracking is active for the variation.
    """

    upc: typing.Optional[str] = pydantic.Field(default=None)
    """
    The universal product code (UPC) of the item variation, if any. This is a searchable attribute for use in applicable query filters.
    
    The value of this attribute should be a number of 12-14 digits long.  This restriction is enforced on the Square Seller Dashboard,
    Square Point of Sale or Retail Point of Sale apps, where this attribute shows in the GTIN field. If a non-compliant UPC value is assigned
    to this attribute using the API, the value is not editable on the Seller Dashboard, Square Point of Sale or Retail Point of Sale apps
    unless it is updated to fit the expected format.
    """

    user_data: typing.Optional[str] = pydantic.Field(default=None)
    """
    Arbitrary user metadata to associate with the item variation. This attribute value length is of Unicode code points.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
