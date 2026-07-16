

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StackSetSummaryDriftStatus(str, enum.Enum):
    """
    <p>Status of the stack set's actual configuration compared to its expected template and parameter configuration. A stack set is considered to have drifted if one or more of its stack instances have drifted from their expected template and parameter configuration.</p> <ul> <li> <p> <code>DRIFTED</code>: One or more of the stack instances belonging to the stack set stack differs from the expected template and parameter configuration. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked the stack set for drift.</p> </li> <li> <p> <code>IN_SYNC</code>: All the stack instances belonging to the stack set stack match from the expected template and parameter configuration.</p> </li> <li> <p> <code>UNKNOWN</code>: This value is reserved for future use.</p> </li> </ul>
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
        if self is StackSetSummaryDriftStatus.DRIFTED:
            return drifted()
        if self is StackSetSummaryDriftStatus.IN_SYNC:
            return in_sync()
        if self is StackSetSummaryDriftStatus.UNKNOWN:
            return unknown()
        if self is StackSetSummaryDriftStatus.NOT_CHECKED:
            return not_checked()
