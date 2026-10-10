

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ConvertRequestValidate(enum.StrEnum):
    ON = "on"

    def visit(self, on: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConvertRequestValidate.ON:
            return on()
