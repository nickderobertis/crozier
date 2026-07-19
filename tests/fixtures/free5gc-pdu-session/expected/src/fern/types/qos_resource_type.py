

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QosResourceType(enum.StrEnum):
    NON_GBR = "NON_GBR"
    NON_CRITICAL_GBR = "NON_CRITICAL_GBR"
    CRITICAL_GBR = "CRITICAL_GBR"

    def visit(
        self,
        non_gbr: typing.Callable[[], T_Result],
        non_critical_gbr: typing.Callable[[], T_Result],
        critical_gbr: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QosResourceType.NON_GBR:
            return non_gbr()
        if self is QosResourceType.NON_CRITICAL_GBR:
            return non_critical_gbr()
        if self is QosResourceType.CRITICAL_GBR:
            return critical_gbr()
