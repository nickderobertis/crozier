

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sign_token_payload_payload import SignTokenPayloadPayload


class SignTokenPayload(UniversalBaseModel):
    """
    The POST body for the request to generate a signed token
    """

    payload: SignTokenPayloadPayload = pydantic.Field()
    """
    The payload of the token signing request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
