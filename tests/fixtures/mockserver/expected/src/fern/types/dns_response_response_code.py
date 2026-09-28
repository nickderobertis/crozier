

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DnsResponseResponseCode(enum.StrEnum):
    NOERROR = "NOERROR"
    FORMERR = "FORMERR"
    SERVFAIL = "SERVFAIL"
    NXDOMAIN = "NXDOMAIN"
    NOTIMP = "NOTIMP"
    REFUSED = "REFUSED"

    def visit(
        self,
        noerror: typing.Callable[[], T_Result],
        formerr: typing.Callable[[], T_Result],
        servfail: typing.Callable[[], T_Result],
        nxdomain: typing.Callable[[], T_Result],
        notimp: typing.Callable[[], T_Result],
        refused: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DnsResponseResponseCode.NOERROR:
            return noerror()
        if self is DnsResponseResponseCode.FORMERR:
            return formerr()
        if self is DnsResponseResponseCode.SERVFAIL:
            return servfail()
        if self is DnsResponseResponseCode.NXDOMAIN:
            return nxdomain()
        if self is DnsResponseResponseCode.NOTIMP:
            return notimp()
        if self is DnsResponseResponseCode.REFUSED:
            return refused()
