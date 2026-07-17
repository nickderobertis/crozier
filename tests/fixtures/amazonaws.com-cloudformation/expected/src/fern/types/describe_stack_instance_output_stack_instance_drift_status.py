

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DescribeStackInstanceOutputStackInstanceDriftStatus(enum.StrEnum):
    """
    <p>Status of the stack instance's actual configuration compared to the expected template and parameter configuration of the stack set to which it belongs.</p> <ul> <li> <p> <code>DRIFTED</code>: The stack differs from the expected template and parameter configuration of the stack set to which it belongs. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked if the stack instance differs from its expected stack set configuration.</p> </li> <li> <p> <code>IN_SYNC</code>: The stack instance's actual configuration matches its expected stack set configuration.</p> </li> <li> <p> <code>UNKNOWN</code>: This value is reserved for future use.</p> </li> </ul>
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
        if self is DescribeStackInstanceOutputStackInstanceDriftStatus.DRIFTED:
            return drifted()
        if self is DescribeStackInstanceOutputStackInstanceDriftStatus.IN_SYNC:
            return in_sync()
        if self is DescribeStackInstanceOutputStackInstanceDriftStatus.UNKNOWN:
            return unknown()
        if self is DescribeStackInstanceOutputStackInstanceDriftStatus.NOT_CHECKED:
            return not_checked()
