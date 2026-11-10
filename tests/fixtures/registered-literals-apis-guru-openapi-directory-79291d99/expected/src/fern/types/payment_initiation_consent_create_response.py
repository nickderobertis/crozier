

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_initiation_consent_status import PaymentInitiationConsentStatus
from .request_id import RequestId


class PaymentInitiationConsentCreateResponse(UniversalBaseModel):
    """
    PaymentInitiationConsentCreateResponse defines the response schema for `/payment_initiation/consent/create`
    """

    consent_id: str = pydantic.Field()
    """
    A unique ID identifying the payment consent.
    """

    request_id: RequestId
    status: PaymentInitiationConsentStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
