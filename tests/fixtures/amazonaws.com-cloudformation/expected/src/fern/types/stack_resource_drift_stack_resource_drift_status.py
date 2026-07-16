

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackResourceDriftStackResourceDriftStatus(enum.StrEnum):
    """
    <p>Status of the resource's actual configuration compared to its expected configuration.</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected template configuration because the resource has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: One or more resource properties differ from their expected values (as defined in the stack template and any values specified as template parameters).</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation does not currently return this value.</p> </li> </ul>
    """

    IN_SYNC = "IN_SYNC"
    MODIFIED = "MODIFIED"
    DELETED = "DELETED"
    NOT_CHECKED = "NOT_CHECKED"

    def visit(
        self,
        in_sync: typing.Callable[[], T_Result],
        modified: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        not_checked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackResourceDriftStackResourceDriftStatus.IN_SYNC:
            return in_sync()
        if self is StackResourceDriftStackResourceDriftStatus.MODIFIED:
            return modified()
        if self is StackResourceDriftStackResourceDriftStatus.DELETED:
            return deleted()
        if self is StackResourceDriftStackResourceDriftStatus.NOT_CHECKED:
            return not_checked()
