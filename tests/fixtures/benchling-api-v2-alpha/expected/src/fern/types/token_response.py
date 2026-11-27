

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .token_response_token_type import TokenResponseTokenType


class TokenResponse(UniversalBaseModel):
    access_token: typing.Optional[str] = None
    expires_in: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of seconds that token is valid for
    """

    token_type: typing.Optional[TokenResponseTokenType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
