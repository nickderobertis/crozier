

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_profile_token import PaymentProfileToken
from .request_id import RequestId


class PaymentProfileCreateResponse(UniversalBaseModel):
    """
    PaymentProfileCreateResponse defines the response schema for `/payment_profile/create`
    """

    payment_profile_token: PaymentProfileToken
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
