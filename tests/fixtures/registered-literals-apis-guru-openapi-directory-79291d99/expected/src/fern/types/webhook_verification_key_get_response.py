

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jwk_public_key import JwkPublicKey
from .request_id import RequestId


class WebhookVerificationKeyGetResponse(UniversalBaseModel):
    """
    WebhookVerificationKeyGetResponse defines the response schema for `/webhook_verification_key/get`
    """

    key: JwkPublicKey
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
