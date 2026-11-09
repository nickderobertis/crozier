

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CallParametersMachineDetection(enum.StrEnum):
    """
    Enables answering machine detection; optionally, it waits until the greeting message has been played back (an Eqivo extension)
    """

    ENABLE = "Enable"
    DETECT_MESSAGE_END = "DetectMessageEnd"

    def visit(
        self, enable: typing.Callable[[], T_Result], detect_message_end: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is CallParametersMachineDetection.ENABLE:
            return enable()
        if self is CallParametersMachineDetection.DETECT_MESSAGE_END:
            return detect_message_end()
