

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackSetOperationResultSummaryAccountGateResultStatus(enum.StrEnum):
    """
    <p>The status of the account gate function.</p> <ul> <li> <p> <code>SUCCEEDED</code>: The account gate function has determined that the account and Region passes any requirements for a stack set operation to occur. CloudFormation proceeds with the stack operation in that account and Region.</p> </li> <li> <p> <code>FAILED</code>: The account gate function has determined that the account and Region doesn't meet the requirements for a stack set operation to occur. CloudFormation cancels the stack set operation in that account and Region, and sets the stack set operation result status for that account and Region to <code>FAILED</code>.</p> </li> <li> <p> <code>SKIPPED</code>: CloudFormation has skipped calling the account gate function for this account and Region, for one of the following reasons:</p> <ul> <li> <p>An account gate function hasn't been specified for the account and Region. CloudFormation proceeds with the stack set operation in this account and Region.</p> </li> <li> <p>The <code>AWSCloudFormationStackSetExecutionRole</code> of the stack set administration account lacks permissions to invoke the function. CloudFormation proceeds with the stack set operation in this account and Region.</p> </li> <li> <p>Either no action is necessary, or no action is possible, on the stack. CloudFormation skips the stack set operation in this account and Region.</p> </li> </ul> </li> </ul>
    """

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"

    def visit(
        self,
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackSetOperationResultSummaryAccountGateResultStatus.SUCCEEDED:
            return succeeded()
        if self is StackSetOperationResultSummaryAccountGateResultStatus.FAILED:
            return failed()
        if self is StackSetOperationResultSummaryAccountGateResultStatus.SKIPPED:
            return skipped()
