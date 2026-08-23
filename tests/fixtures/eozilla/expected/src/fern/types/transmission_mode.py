

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransmissionMode(enum.StrEnum):
    VALUE = "value"
    REFERENCE = "reference"

    def visit(self, value: typing.Callable[[], T_Result], reference: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransmissionMode.VALUE:
            return value()
        if self is TransmissionMode.REFERENCE:
            return reference()
