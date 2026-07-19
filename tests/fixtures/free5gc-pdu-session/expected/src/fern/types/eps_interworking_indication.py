

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EpsInterworkingIndication(enum.StrEnum):
    NONE = "NONE"
    WITH_N26 = "WITH_N26"
    WITHOUT_N26 = "WITHOUT_N26"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        with_n26: typing.Callable[[], T_Result],
        without_n26: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EpsInterworkingIndication.NONE:
            return none()
        if self is EpsInterworkingIndication.WITH_N26:
            return with_n26()
        if self is EpsInterworkingIndication.WITHOUT_N26:
            return without_n26()
