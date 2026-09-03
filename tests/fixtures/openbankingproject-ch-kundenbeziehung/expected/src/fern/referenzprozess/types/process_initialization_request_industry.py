

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ProcessInitializationRequestIndustry(enum.StrEnum):
    """
    Ziel-Ecosystem für den Prozess
    """

    BANKING = "banking"
    INSURANCE = "insurance"
    MOBILITY = "mobility"
    RETAIL = "retail"
    GOVERNMENT = "government"
    HEALTHCARE = "healthcare"

    def visit(
        self,
        banking: typing.Callable[[], T_Result],
        insurance: typing.Callable[[], T_Result],
        mobility: typing.Callable[[], T_Result],
        retail: typing.Callable[[], T_Result],
        government: typing.Callable[[], T_Result],
        healthcare: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProcessInitializationRequestIndustry.BANKING:
            return banking()
        if self is ProcessInitializationRequestIndustry.INSURANCE:
            return insurance()
        if self is ProcessInitializationRequestIndustry.MOBILITY:
            return mobility()
        if self is ProcessInitializationRequestIndustry.RETAIL:
            return retail()
        if self is ProcessInitializationRequestIndustry.GOVERNMENT:
            return government()
        if self is ProcessInitializationRequestIndustry.HEALTHCARE:
            return healthcare()
