

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_initiation_consent_constraints import PaymentInitiationConsentConstraints
from .payment_initiation_consent_scope import PaymentInitiationConsentScope
from .payment_initiation_consent_status import PaymentInitiationConsentStatus


class PaymentInitiationConsent(UniversalBaseModel):
    """
    PaymentInitiationConsent defines a payment initiation consent.
    """

    consent_id: str = pydantic.Field()
    """
    The consent ID.
    """

    constraints: PaymentInitiationConsentConstraints
    created_at: dt.datetime = pydantic.Field()
    """
    Consent creation timestamp, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.
    """

    recipient_id: str = pydantic.Field()
    """
    The ID of the recipient the payment consent is for.
    """

    reference: str = pydantic.Field()
    """
    A reference for the payment consent.
    """

    scopes: typing.List[PaymentInitiationConsentScope] = pydantic.Field()
    """
    An array of payment consent scopes.
    """

    status: PaymentInitiationConsentStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
