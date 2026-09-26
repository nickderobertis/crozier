

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V60TaxabilityCodeRateActionCode(enum.StrEnum):
    """
    Outcome of the TIC lookup: T00 (valid TIC, rules listed), T01 (valid TIC, no applicable rate rules), T02 (invalid TIC), T03 (invalid TIC format).
    """

    T00 = "T00"
    T01 = "T01"
    T02 = "T02"
    T03 = "T03"

    def visit(
        self,
        t00: typing.Callable[[], T_Result],
        t01: typing.Callable[[], T_Result],
        t02: typing.Callable[[], T_Result],
        t03: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V60TaxabilityCodeRateActionCode.T00:
            return t00()
        if self is V60TaxabilityCodeRateActionCode.T01:
            return t01()
        if self is V60TaxabilityCodeRateActionCode.T02:
            return t02()
        if self is V60TaxabilityCodeRateActionCode.T03:
            return t03()
