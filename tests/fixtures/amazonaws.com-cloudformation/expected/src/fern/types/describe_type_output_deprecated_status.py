

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DescribeTypeOutputDeprecatedStatus(str, enum.Enum):
    """
    <p>The deprecation status of the extension version.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension is activated or registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension has been deactivated or deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul> <p>For public third-party extensions, CloudFormation returns <code>null</code>.</p>
    """

    LIVE = "LIVE"
    DEPRECATED = "DEPRECATED"

    def visit(self, live: typing.Callable[[], T_Result], deprecated: typing.Callable[[], T_Result]) -> T_Result:
        if self is DescribeTypeOutputDeprecatedStatus.LIVE:
            return live()
        if self is DescribeTypeOutputDeprecatedStatus.DEPRECATED:
            return deprecated()
