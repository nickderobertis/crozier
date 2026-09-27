

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DnsRecordDnsClass(enum.StrEnum):
    IN = "IN"
    CH = "CH"
    HS = "HS"
    ANY = "ANY"

    def visit(
        self,
        in_: typing.Callable[[], T_Result],
        ch: typing.Callable[[], T_Result],
        hs: typing.Callable[[], T_Result],
        any: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DnsRecordDnsClass.IN:
            return in_()
        if self is DnsRecordDnsClass.CH:
            return ch()
        if self is DnsRecordDnsClass.HS:
            return hs()
        if self is DnsRecordDnsClass.ANY:
            return any()
