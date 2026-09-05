

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IkeGatewaysConfigPeerIdType(enum.StrEnum):
    IPADDR = "ipaddr"
    KEYID = "keyid"
    FQDN = "fqdn"
    UFQDN = "ufqdn"

    def visit(
        self,
        ipaddr: typing.Callable[[], T_Result],
        keyid: typing.Callable[[], T_Result],
        fqdn: typing.Callable[[], T_Result],
        ufqdn: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IkeGatewaysConfigPeerIdType.IPADDR:
            return ipaddr()
        if self is IkeGatewaysConfigPeerIdType.KEYID:
            return keyid()
        if self is IkeGatewaysConfigPeerIdType.FQDN:
            return fqdn()
        if self is IkeGatewaysConfigPeerIdType.UFQDN:
            return ufqdn()
