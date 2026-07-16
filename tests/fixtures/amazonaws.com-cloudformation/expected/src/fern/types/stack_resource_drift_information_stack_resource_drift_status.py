

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackResourceDriftInformationStackResourceDriftStatus(enum.StrEnum):
    """
    <p>Status of the resource's actual configuration compared to its expected configuration</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected configuration in that it has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: The resource differs from its expected configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation has not checked if the resource differs from its expected configuration.</p> <p>Any resources that do not currently support drift detection have a status of <code>NOT_CHECKED</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected configuration.</p> </li> </ul>
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
        if self is StackResourceDriftInformationStackResourceDriftStatus.IN_SYNC:
            return in_sync()
        if self is StackResourceDriftInformationStackResourceDriftStatus.MODIFIED:
            return modified()
        if self is StackResourceDriftInformationStackResourceDriftStatus.DELETED:
            return deleted()
        if self is StackResourceDriftInformationStackResourceDriftStatus.NOT_CHECKED:
            return not_checked()
