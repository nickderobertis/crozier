

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventType(enum.StrEnum):
    FORM_RESPONSE = "FORM_RESPONSE"

    def visit(self, form_response: typing.Callable[[], T_Result]) -> T_Result:
        if self is EventType.FORM_RESPONSE:
            return form_response()
