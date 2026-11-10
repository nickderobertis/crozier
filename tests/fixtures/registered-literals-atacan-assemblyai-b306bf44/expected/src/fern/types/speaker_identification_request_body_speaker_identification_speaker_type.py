

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SpeakerIdentificationRequestBodySpeakerIdentificationSpeakerType(enum.StrEnum):
    """
    Type of speaker identification
    """

    ROLE = "role"
    NAME = "name"

    def visit(self, role: typing.Callable[[], T_Result], name: typing.Callable[[], T_Result]) -> T_Result:
        if self is SpeakerIdentificationRequestBodySpeakerIdentificationSpeakerType.ROLE:
            return role()
        if self is SpeakerIdentificationRequestBodySpeakerIdentificationSpeakerType.NAME:
            return name()
