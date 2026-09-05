

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ike import Ike
from .ipsec_tunnel_crypto import IpsecTunnelCrypto
from .ipsec_tunnel_tunnel_monitor import IpsecTunnelTunnelMonitor


class IpsecTunnel(UniversalBaseModel):
    anti_replay: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable Anti-Replay check on this tunnel
    """

    copy_tos: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Copy IP TOS bits from inner packet to IPSec packet (not recommended)
    """

    crypto: typing.Optional[IpsecTunnelCrypto] = None
    enable_gre_encapsulation: typing.Optional[bool] = pydantic.Field(default=None)
    """
    allow GRE over IPSec
    """

    ike: Ike
    tunnel_monitor: typing.Optional[IpsecTunnelTunnelMonitor] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
