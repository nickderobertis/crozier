

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DnsRecordType(enum.StrEnum):
    A = "A"
    AAAA = "AAAA"
    CNAME = "CNAME"
    MX = "MX"
    SRV = "SRV"
    TXT = "TXT"
    PTR = "PTR"

    def visit(
        self,
        a: typing.Callable[[], T_Result],
        aaaa: typing.Callable[[], T_Result],
        cname: typing.Callable[[], T_Result],
        mx: typing.Callable[[], T_Result],
        srv: typing.Callable[[], T_Result],
        txt: typing.Callable[[], T_Result],
        ptr: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DnsRecordType.A:
            return a()
        if self is DnsRecordType.AAAA:
            return aaaa()
        if self is DnsRecordType.CNAME:
            return cname()
        if self is DnsRecordType.MX:
            return mx()
        if self is DnsRecordType.SRV:
            return srv()
        if self is DnsRecordType.TXT:
            return txt()
        if self is DnsRecordType.PTR:
            return ptr()
