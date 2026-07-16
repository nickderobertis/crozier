

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1money import V1Money
from .v1payment_surcharge import V1PaymentSurcharge
from .v1payment_tax import V1PaymentTax


class V1Refund(UniversalBaseModel):
    """
    V1Refund
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the merchant initiated the refund for Square to process, in ISO 8601 format.
    """

    is_exchange: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether or not the refund is associated with an exchange. If is_exchange is true, the refund reflects the value of goods returned in the exchange not the total money refunded.
    """

    merchant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A Square-issued ID associated with the refund. For single-tender refunds, payment_id is the ID of the original payment ID. For split-tender refunds, payment_id is the ID of the original tender. For exchange-based refunds (is_exchange == true), payment_id is the ID of the original payment ID even if the payment includes other tenders.
    """

    processed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when Square processed the refund on behalf of the merchant, in ISO 8601 format.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The merchant-specified reason for the refund.
    """

    refunded_additive_tax: typing.Optional[typing.List[V1PaymentTax]] = pydantic.Field(default=None)
    """
    All of the additive taxes associated with the refund.
    """

    refunded_additive_tax_money: typing.Optional[V1Money] = None
    refunded_discount_money: typing.Optional[V1Money] = None
    refunded_inclusive_tax: typing.Optional[typing.List[V1PaymentTax]] = pydantic.Field(default=None)
    """
    All of the inclusive taxes associated with the refund.
    """

    refunded_inclusive_tax_money: typing.Optional[V1Money] = None
    refunded_money: typing.Optional[V1Money] = None
    refunded_processing_fee_money: typing.Optional[V1Money] = None
    refunded_surcharge_money: typing.Optional[V1Money] = None
    refunded_surcharges: typing.Optional[typing.List[V1PaymentSurcharge]] = pydantic.Field(default=None)
    """
    A list of all surcharges associated with the refund.
    """

    refunded_tax_money: typing.Optional[V1Money] = None
    refunded_tip_money: typing.Optional[V1Money] = None
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of refund
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
