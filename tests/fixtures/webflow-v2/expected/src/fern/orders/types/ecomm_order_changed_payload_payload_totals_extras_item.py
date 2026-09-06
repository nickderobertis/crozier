

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ecomm_order_changed_payload_payload_totals_extras_item_price import (
    EcommOrderChangedPayloadPayloadTotalsExtrasItemPrice,
)
from .ecomm_order_changed_payload_payload_totals_extras_item_type import (
    EcommOrderChangedPayloadPayloadTotalsExtrasItemType,
)


class EcommOrderChangedPayloadPayloadTotalsExtrasItem(UniversalBaseModel):
    """
    Extra order items, includes discounts, shipping, and taxes.
    """

    type: typing.Optional[EcommOrderChangedPayloadPayloadTotalsExtrasItemType] = pydantic.Field(default=None)
    """
    The type of extra item this is.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable (but English) name for this extra charge.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable (but English) description of this extra charge.
    """

    price: typing.Optional[EcommOrderChangedPayloadPayloadTotalsExtrasItemPrice] = pydantic.Field(default=None)
    """
    The price for the item
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
