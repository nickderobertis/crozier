

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_initiation_maximum_payment_amount import PaymentInitiationMaximumPaymentAmount
from .payment_initiation_standing_order_metadata import PaymentInitiationStandingOrderMetadata


class PaymentInitiationMetadata(UniversalBaseModel):
    """
    Metadata that captures what specific payment configurations an institution supports when making Payment Initiation requests.
    """

    maximum_payment_amount: PaymentInitiationMaximumPaymentAmount
    standing_order_metadata: typing.Optional[PaymentInitiationStandingOrderMetadata] = None
    supports_international_payments: bool = pydantic.Field()
    """
    Indicates whether the institution supports payments from a different country.
    """

    supports_refund_details: bool = pydantic.Field()
    """
    Indicates whether the institution supports returning refund details when initiating a payment.
    """

    supports_sepa_instant: bool = pydantic.Field()
    """
    Indicates whether the institution supports SEPA Instant payments.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
