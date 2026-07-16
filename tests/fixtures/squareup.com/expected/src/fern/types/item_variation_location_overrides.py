

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class ItemVariationLocationOverrides(UniversalBaseModel):
    """
    Price and inventory alerting overrides for a `CatalogItemVariation` at a specific `Location`.
    """

    inventory_alert_threshold: typing.Optional[int] = pydantic.Field(default=None)
    """
    If the inventory quantity for the variation is less than or equal to this value and `inventory_alert_type`
    is `LOW_QUANTITY`, the variation displays an alert in the merchant dashboard.
    
    This value is always an integer.
    """

    inventory_alert_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates whether the `CatalogItemVariation` displays an alert when its inventory
    quantity is less than or equal to its `inventory_alert_threshold`.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the `Location`. This can include locations that are deactivated.
    """

    price_money: typing.Optional[Money] = None
    pricing_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pricing type (fixed or variable) for the `CatalogItemVariation` at the given `Location`.
    """

    track_inventory: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, inventory tracking is active for the `CatalogItemVariation` at this `Location`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
