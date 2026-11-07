

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateVoiceRequestVoiceType(enum.StrEnum):
    RAPID = "rapid"
    PROFESSIONAL = "professional"

    def visit(self, rapid: typing.Callable[[], T_Result], professional: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateVoiceRequestVoiceType.RAPID:
            return rapid()
        if self is CreateVoiceRequestVoiceType.PROFESSIONAL:
            return professional()
