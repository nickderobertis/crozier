

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OAuth2TokenResponse(UniversalBaseModel):
    access_token: str = pydantic.Field()
    """
    The issued access token
    """

    expires_in: int = pydantic.Field()
    """
    Lifetime in seconds of the access token.
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    Granted scopes (space-delimited).
    """

    token_type: str = pydantic.Field()
    """
    Usually 'bearer'
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
