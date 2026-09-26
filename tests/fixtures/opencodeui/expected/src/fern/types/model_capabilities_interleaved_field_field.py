

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelCapabilitiesInterleavedFieldField(enum.StrEnum):
    REASONING_CONTENT = "reasoning_content"
    REASONING_DETAILS = "reasoning_details"

    def visit(
        self, reasoning_content: typing.Callable[[], T_Result], reasoning_details: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ModelCapabilitiesInterleavedFieldField.REASONING_CONTENT:
            return reasoning_content()
        if self is ModelCapabilitiesInterleavedFieldField.REASONING_DETAILS:
            return reasoning_details()
