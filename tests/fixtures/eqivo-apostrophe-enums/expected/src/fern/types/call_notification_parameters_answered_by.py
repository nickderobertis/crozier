

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CallNotificationParametersAnsweredBy(enum.StrEnum):
    """
    Answering actor, when answering machine detection is enabled
    """

    MACHINE_START = "machine_start"
    MACHINE_END_BEEP = "machine_end_beep"
    MACHINE_END_OTHER = "machine_end_other"
    HUMAN = "human"
    UNKNOWN = "unknown"

    def visit(
        self,
        machine_start: typing.Callable[[], T_Result],
        machine_end_beep: typing.Callable[[], T_Result],
        machine_end_other: typing.Callable[[], T_Result],
        human: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CallNotificationParametersAnsweredBy.MACHINE_START:
            return machine_start()
        if self is CallNotificationParametersAnsweredBy.MACHINE_END_BEEP:
            return machine_end_beep()
        if self is CallNotificationParametersAnsweredBy.MACHINE_END_OTHER:
            return machine_end_other()
        if self is CallNotificationParametersAnsweredBy.HUMAN:
            return human()
        if self is CallNotificationParametersAnsweredBy.UNKNOWN:
            return unknown()
