

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ServerConfig(UniversalBaseModel):
    """
    Server configuration for opencode serve and web commands
    """

    port: typing.Optional[int] = pydantic.Field(default=None)
    """
    Port to listen on
    """

    hostname: typing.Optional[str] = pydantic.Field(default=None)
    """
    Hostname to listen on
    """

    mdns: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable mDNS service discovery
    """

    cors: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Additional domains to allow for CORS
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
