

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_consent_max_payment_amount import PaymentConsentMaxPaymentAmount
from .payment_consent_periodic_amount import PaymentConsentPeriodicAmount
from .payment_consent_valid_date_time import PaymentConsentValidDateTime


class PaymentInitiationConsentConstraints(UniversalBaseModel):
    """
    Limitations that will be applied to payments initiated using the payment consent.
    """

    max_payment_amount: PaymentConsentMaxPaymentAmount
    periodic_amounts: typing.List[PaymentConsentPeriodicAmount] = pydantic.Field()
    """
    A list of amount limitations per period of time.
    """

    valid_date_time: typing.Optional[PaymentConsentValidDateTime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
