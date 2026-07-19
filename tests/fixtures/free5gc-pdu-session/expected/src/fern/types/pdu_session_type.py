

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PduSessionType(enum.StrEnum):
    IPV4 = "IPV4"
    IPV6 = "IPV6"
    IPV4V6 = "IPV4V6"
    UNSTRUCTURED = "UNSTRUCTURED"
    ETHERNET = "ETHERNET"

    def visit(
        self,
        ipv4: typing.Callable[[], T_Result],
        ipv6: typing.Callable[[], T_Result],
        ipv4v6: typing.Callable[[], T_Result],
        unstructured: typing.Callable[[], T_Result],
        ethernet: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PduSessionType.IPV4:
            return ipv4()
        if self is PduSessionType.IPV6:
            return ipv6()
        if self is PduSessionType.IPV4V6:
            return ipv4v6()
        if self is PduSessionType.UNSTRUCTURED:
            return unstructured()
        if self is PduSessionType.ETHERNET:
            return ethernet()
