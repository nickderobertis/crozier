

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .payment_initiation_consent import PaymentInitiationConsent
from .request_id import RequestId


class PaymentInitiationConsentGetResponse(PaymentInitiationConsent):
    """
    PaymentInitiationConsentGetResponse defines the response schema for `/payment_initation/consent/get`
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
