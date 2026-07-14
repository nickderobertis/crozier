

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PushToken(UniversalBaseModel):
    """
    PushToken in JWT format, self-signed.
    """

    aud: str = pydantic.Field()
    """
    audience (URI)
    """

    exp: typing.Optional[int] = None
    iat: typing.Optional[int] = None
    iss: str = pydantic.Field()
    """
    issuer (URI)
    """

    nbf: typing.Optional[int] = None
    sub: str = pydantic.Field()
    """
    UUID and public signing key
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
