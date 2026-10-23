

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AccessToken(UniversalBaseModel):
    access_token: str = pydantic.Field()
    """
    connection string credentials or standard access token (CSP dependent)
    """

    token_type: str = pydantic.Field()
    """
    token type (Bearer, SasUrl, ....).
    """

    expires_in: float = pydantic.Field()
    """
    expiration time (in minutes) of the connection string credentials
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
