

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AuthentiqId(UniversalBaseModel):
    """
    Authentiq ID in JWT format, self-signed.
    """

    devtoken: typing.Optional[str] = pydantic.Field(default=None)
    """
    device token for push messages
    """

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
