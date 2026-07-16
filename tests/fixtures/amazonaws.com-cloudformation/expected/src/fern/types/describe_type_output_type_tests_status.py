

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DescribeTypeOutputTypeTestsStatus(enum.StrEnum):
    """
    <p>The contract test status of the registered extension version. To return the extension test status of a specific extension version, you must specify <code>VersionId</code>.</p> <p>This applies only to registered private extension versions. CloudFormation doesn't return this information for public extensions, whether they are activated in your account.</p> <ul> <li> <p> <code>PASSED</code>: The extension has passed all its contract tests.</p> <p>An extension must have a test status of <code>PASSED</code> before it can be published. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation Command Line Interface User Guide</i>.</p> </li> <li> <p> <code>FAILED</code>: The extension has failed one or more contract tests.</p> </li> <li> <p> <code>IN_PROGRESS</code>: Contract tests are currently being performed on the extension.</p> </li> <li> <p> <code>NOT_TESTED</code>: Contract tests haven't been performed on the extension.</p> </li> </ul>
    """

    PASSED = "PASSED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    NOT_TESTED = "NOT_TESTED"

    def visit(
        self,
        passed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        not_tested: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DescribeTypeOutputTypeTestsStatus.PASSED:
            return passed()
        if self is DescribeTypeOutputTypeTestsStatus.FAILED:
            return failed()
        if self is DescribeTypeOutputTypeTestsStatus.IN_PROGRESS:
            return in_progress()
        if self is DescribeTypeOutputTypeTestsStatus.NOT_TESTED:
            return not_tested()
