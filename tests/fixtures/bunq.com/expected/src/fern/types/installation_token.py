

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InstallationToken(UniversalBaseModel):
    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the Token's creation.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the Token.
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The installation token is the token the client has to provide in the "X-Bunq-Client-Authentication" header for the creation of a DeviceServer and SessionServer.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the Token's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
