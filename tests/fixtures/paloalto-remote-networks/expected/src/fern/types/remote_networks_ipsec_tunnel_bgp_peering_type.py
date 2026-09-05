

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteNetworksIpsecTunnelBgpPeeringType(enum.StrEnum):
    """
    Exchange Routes: exchange-v4-over-v4 stands for Exchange IPv4 routes over IPv4 peering. exchange-v4-v6-over-v4 stands for Exchange both IPv4 and IPv6 routes over IPv4 peering. exchange-v4-over-v4-v6-over-v6 stands for Exchange IPv4 routes over IPv4 peer and IPv6 route over IPv6 peer. exchange-v6-over-v6 stands for Exchange IPv6 routes over IPv6 peering.
    """

    EXCHANGE_V4OVER_V4 = "exchange-v4-over-v4"
    EXCHANGE_V4V6OVER_V4 = "exchange-v4-v6-over-v4"
    EXCHANGE_V4OVER_V4V6OVER_V6 = "exchange-v4-over-v4-v6-over-v6"
    EXCHANGE_V6OVER_V6 = "exchange-v6-over-v6"

    def visit(
        self,
        exchange_v4over_v4: typing.Callable[[], T_Result],
        exchange_v4v6over_v4: typing.Callable[[], T_Result],
        exchange_v4over_v4v6over_v6: typing.Callable[[], T_Result],
        exchange_v6over_v6: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RemoteNetworksIpsecTunnelBgpPeeringType.EXCHANGE_V4OVER_V4:
            return exchange_v4over_v4()
        if self is RemoteNetworksIpsecTunnelBgpPeeringType.EXCHANGE_V4V6OVER_V4:
            return exchange_v4v6over_v4()
        if self is RemoteNetworksIpsecTunnelBgpPeeringType.EXCHANGE_V4OVER_V4V6OVER_V6:
            return exchange_v4over_v4v6over_v6()
        if self is RemoteNetworksIpsecTunnelBgpPeeringType.EXCHANGE_V6OVER_V6:
            return exchange_v6over_v6()
