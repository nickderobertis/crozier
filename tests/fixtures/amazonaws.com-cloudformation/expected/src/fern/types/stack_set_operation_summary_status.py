

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackSetOperationSummaryStatus(enum.StrEnum):
    """
    <p>The overall status of the operation.</p> <ul> <li> <p> <code>FAILED</code>: The operation exceeded the specified failure tolerance. The failure tolerance value that you've set for an operation is applied for each Region during stack create and update operations. If the number of failed stacks within a Region exceeds the failure tolerance, the status of the operation in the Region is set to <code>FAILED</code>. This in turn sets the status of the operation as a whole to <code>FAILED</code>, and CloudFormation cancels the operation in any remaining Regions.</p> </li> <li> <p> <code>QUEUED</code>: [Service-managed permissions] For automatic deployments that require a sequence of operations, the operation is queued to be performed. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-status-codes">stack set operation status codes</a> in the CloudFormation User Guide.</p> </li> <li> <p> <code>RUNNING</code>: The operation is currently being performed.</p> </li> <li> <p> <code>STOPPED</code>: The user has canceled the operation.</p> </li> <li> <p> <code>STOPPING</code>: The operation is in the process of stopping, at user request.</p> </li> <li> <p> <code>SUCCEEDED</code>: The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation.</p> </li> </ul>
    """

    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    QUEUED = "QUEUED"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        stopping: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackSetOperationSummaryStatus.RUNNING:
            return running()
        if self is StackSetOperationSummaryStatus.SUCCEEDED:
            return succeeded()
        if self is StackSetOperationSummaryStatus.FAILED:
            return failed()
        if self is StackSetOperationSummaryStatus.STOPPING:
            return stopping()
        if self is StackSetOperationSummaryStatus.STOPPED:
            return stopped()
        if self is StackSetOperationSummaryStatus.QUEUED:
            return queued()
