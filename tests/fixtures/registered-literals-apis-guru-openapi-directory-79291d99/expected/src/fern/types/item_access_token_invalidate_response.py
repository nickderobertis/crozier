

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_token import AccessToken
from .request_id import RequestId


class ItemAccessTokenInvalidateResponse(UniversalBaseModel):
    """
    ItemAccessTokenInvalidateResponse defines the response schema for `/item/access_token/invalidate`
    """

    new_access_token: AccessToken
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
