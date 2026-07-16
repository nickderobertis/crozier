

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObExternalScheduleType1Code(str, enum.Enum):
    """
    Specifies the scheduled payment date type requested
    """

    ARRIVAL = "Arrival"
    EXECUTION = "Execution"

    def visit(self, arrival: typing.Callable[[], T_Result], execution: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObExternalScheduleType1Code.ARRIVAL:
            return arrival()
        if self is ObExternalScheduleType1Code.EXECUTION:
            return execution()
