

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class SandboxPublicTokenCreateResponse(UniversalBaseModel):
    """
    SandboxPublicTokenCreateResponse defines the response schema for `/sandbox/public_token/create`
    """

    public_token: str = pydantic.Field()
    """
    A public token that can be exchanged for an access token using `/item/public_token/exchange`
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
