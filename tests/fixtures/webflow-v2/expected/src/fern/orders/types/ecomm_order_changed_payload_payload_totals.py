

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ecomm_order_changed_payload_payload_totals_extras_item import EcommOrderChangedPayloadPayloadTotalsExtrasItem
from .ecomm_order_changed_payload_payload_totals_subtotal import EcommOrderChangedPayloadPayloadTotalsSubtotal
from .ecomm_order_changed_payload_payload_totals_total import EcommOrderChangedPayloadPayloadTotalsTotal


class EcommOrderChangedPayloadPayloadTotals(UniversalBaseModel):
    """
    An object describing various pricing totals
    """

    subtotal: typing.Optional[EcommOrderChangedPayloadPayloadTotalsSubtotal] = pydantic.Field(default=None)
    """
    The subtotal price
    """

    extras: typing.Optional[typing.List[EcommOrderChangedPayloadPayloadTotalsExtrasItem]] = pydantic.Field(default=None)
    """
    An array of extra items, includes discounts, shipping, and taxes.
    """

    total: typing.Optional[EcommOrderChangedPayloadPayloadTotalsTotal] = pydantic.Field(default=None)
    """
    The total price
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
