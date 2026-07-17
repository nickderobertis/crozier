

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackSummaryDriftInformationStackDriftStatus(enum.StrEnum):
    """
    <p>Status of the stack's actual configuration compared to its expected template configuration.</p> <ul> <li> <p> <code>DRIFTED</code>: The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked if the stack differs from its expected template configuration.</p> </li> <li> <p> <code>IN_SYNC</code>: The stack's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>UNKNOWN</code>: This value is reserved for future use.</p> </li> </ul>
    """

    DRIFTED = "DRIFTED"
    IN_SYNC = "IN_SYNC"
    UNKNOWN = "UNKNOWN"
    NOT_CHECKED = "NOT_CHECKED"

    def visit(
        self,
        drifted: typing.Callable[[], T_Result],
        in_sync: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        not_checked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackSummaryDriftInformationStackDriftStatus.DRIFTED:
            return drifted()
        if self is StackSummaryDriftInformationStackDriftStatus.IN_SYNC:
            return in_sync()
        if self is StackSummaryDriftInformationStackDriftStatus.UNKNOWN:
            return unknown()
        if self is StackSummaryDriftInformationStackDriftStatus.NOT_CHECKED:
            return not_checked()
