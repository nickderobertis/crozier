

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .otoroshi_tcp_tcp_target_ip import OtoroshiTcpTcpTargetIp


class OtoroshiTcpTcpTarget(UniversalBaseModel):
    """
    Target for a TCP proxy
    """

    host: typing.Optional[str] = pydantic.Field(default=None)
    """
    Target host
    """

    ip: typing.Optional[OtoroshiTcpTcpTargetIp] = pydantic.Field(default=None)
    """
    Target ip
    """

    port: typing.Optional[int] = pydantic.Field(default=None)
    """
    Target port
    """

    tls: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Use tls
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
