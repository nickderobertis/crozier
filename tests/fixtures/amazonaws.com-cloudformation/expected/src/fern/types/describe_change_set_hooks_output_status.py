

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DescribeChangeSetHooksOutputStatus(str, enum.Enum):
    """
    Provides the status of the change set hook.
    """

    PLANNING = "PLANNING"
    PLANNED = "PLANNED"
    UNAVAILABLE = "UNAVAILABLE"

    def visit(
        self,
        planning: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DescribeChangeSetHooksOutputStatus.PLANNING:
            return planning()
        if self is DescribeChangeSetHooksOutputStatus.PLANNED:
            return planned()
        if self is DescribeChangeSetHooksOutputStatus.UNAVAILABLE:
            return unavailable()
