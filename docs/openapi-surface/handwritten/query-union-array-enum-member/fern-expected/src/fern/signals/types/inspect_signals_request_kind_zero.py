

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class InspectSignalsRequestKindZero(enum.StrEnum):
    OPTICAL = "optical"
    RADIO = "radio"

    def visit(self, optical: typing.Callable[[], T_Result], radio: typing.Callable[[], T_Result]) -> T_Result:
        if self is InspectSignalsRequestKindZero.OPTICAL:
            return optical()
        if self is InspectSignalsRequestKindZero.RADIO:
            return radio()
