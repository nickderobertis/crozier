

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftStatus(enum.StrEnum):
    """
    <p>Status of the stack set's actual configuration compared to its expected template and parameter configuration. A stack set is considered to have drifted if one or more of its stack instances have drifted from their expected template and parameter configuration.</p> <ul> <li> <p> <code>DRIFTED</code>: One or more of the stack instances belonging to the stack set stack differs from the expected template and parameter configuration. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked the stack set for drift.</p> </li> <li> <p> <code>IN_SYNC</code>: All of the stack instances belonging to the stack set stack match from the expected template and parameter configuration.</p> </li> </ul>
    """

    DRIFTED = "DRIFTED"
    IN_SYNC = "IN_SYNC"
    NOT_CHECKED = "NOT_CHECKED"

    def visit(
        self,
        drifted: typing.Callable[[], T_Result],
        in_sync: typing.Callable[[], T_Result],
        not_checked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftStatus.DRIFTED:
            return drifted()
        if self is DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftStatus.IN_SYNC:
            return in_sync()
        if self is DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftStatus.NOT_CHECKED:
            return not_checked()
