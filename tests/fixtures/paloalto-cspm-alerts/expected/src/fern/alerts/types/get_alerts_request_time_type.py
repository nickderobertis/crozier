

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAlertsRequestTimeType(enum.StrEnum):
    RELATIVE = "relative"

    def visit(self, relative: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetAlertsRequestTimeType.RELATIVE:
            return relative()
