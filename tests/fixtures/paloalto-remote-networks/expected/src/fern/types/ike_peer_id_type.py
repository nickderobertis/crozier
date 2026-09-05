

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IkePeerIdType(enum.StrEnum):
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
        if self is IkePeerIdType.IPADDR:
            return ipaddr()
        if self is IkePeerIdType.KEYID:
            return keyid()
        if self is IkePeerIdType.FQDN:
            return fqdn()
        if self is IkePeerIdType.UFQDN:
            return ufqdn()
