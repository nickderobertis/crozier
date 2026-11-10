

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_consent_periodic_alignment import PaymentConsentPeriodicAlignment
from .payment_consent_periodic_amount_amount import PaymentConsentPeriodicAmountAmount
from .payment_consent_periodic_interval import PaymentConsentPeriodicInterval


class PaymentConsentPeriodicAmount(UniversalBaseModel):
    """
    Defines consent payments limitations per period.
    """

    alignment: PaymentConsentPeriodicAlignment
    amount: PaymentConsentPeriodicAmountAmount
    interval: PaymentConsentPeriodicInterval

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
