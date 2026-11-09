

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .token_scope import TokenScope


class Token(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Token Id
    """

    token_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the Token
    """

    created: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Denotes when the token was created
    """

    token_expire: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Denotes when the token was created
    """

    scope: typing.Optional[TokenScope] = pydantic.Field(default=None)
    """
    Scope of the token
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Scope of the token
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
