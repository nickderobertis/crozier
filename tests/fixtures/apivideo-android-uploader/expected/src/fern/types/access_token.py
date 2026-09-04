

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AccessToken(UniversalBaseModel):
    access_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The access token containing security credentials allowing you to acccess the API. The token lasts for one hour.
    """

    token_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of token you have.
    """

    refresh_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    A token you can use to get the next access token when your current access token expires.
    """

    expires_in: typing.Optional[int] = pydantic.Field(default=None)
    """
    Lists the time in seconds when your access token expires. It lasts for one hour.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
