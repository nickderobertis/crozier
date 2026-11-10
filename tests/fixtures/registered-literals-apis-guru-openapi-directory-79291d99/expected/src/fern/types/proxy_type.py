

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProxyType(enum.StrEnum):
    """
    An enum indicating whether a network proxy is present and if so what type it is.

    `none_detected` indicates the user is not on a detectable proxy network.

    `tor` indicates the user was using a Tor browser, which sends encrypted traffic on a decentralized network and is somewhat similar to a VPN (Virtual Private Network).

    `vpn` indicates the user is on a VPN (Virtual Private Network)

    `web_proxy` indicates the user is on a web proxy server, which may allow them to conceal information such as their IP address or other identifying information.

    `public_proxy` indicates the user is on a public web proxy server, which is similar to a web proxy but can be shared by multiple users. This may allow multiple users to appear as if they have the same IP address for instance.
    """

    NONE_DETECTED = "none_detected"
    TOR = "tor"
    VPN = "vpn"
    WEB_PROXY = "web_proxy"
    PUBLIC_PROXY = "public_proxy"

    def visit(
        self,
        none_detected: typing.Callable[[], T_Result],
        tor: typing.Callable[[], T_Result],
        vpn: typing.Callable[[], T_Result],
        web_proxy: typing.Callable[[], T_Result],
        public_proxy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProxyType.NONE_DETECTED:
            return none_detected()
        if self is ProxyType.TOR:
            return tor()
        if self is ProxyType.VPN:
            return vpn()
        if self is ProxyType.WEB_PROXY:
            return web_proxy()
        if self is ProxyType.PUBLIC_PROXY:
            return public_proxy()
