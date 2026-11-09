

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class PaymentInitiationRecipientCreateResponse(UniversalBaseModel):
    """
    PaymentInitiationRecipientCreateResponse defines the response schema for `/payment_initation/recipient/create`
    """

    recipient_id: str = pydantic.Field()
    """
    A unique ID identifying the recipient
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
