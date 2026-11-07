

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .token_request_token_scope import TokenRequestTokenScope


class TokenRequest(UniversalBaseModel):
    token_name: str = pydantic.Field()
    """
    Friendly name of the token
    """

    token_scope: TokenRequestTokenScope = pydantic.Field()
    """
    The scope of the token.
    """

    token_expire: dt.date = pydantic.Field()
    """
    Date when the token must expire (default max 30 days).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
