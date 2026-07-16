

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListTypeVersionsInputDeprecatedStatus(str, enum.Enum):
    """
    <p>The deprecation status of the extension versions that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension version is registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension version has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul> <p>The default is <code>LIVE</code>.</p>
    """

    LIVE = "LIVE"
    DEPRECATED = "DEPRECATED"

    def visit(self, live: typing.Callable[[], T_Result], deprecated: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListTypeVersionsInputDeprecatedStatus.LIVE:
            return live()
        if self is ListTypeVersionsInputDeprecatedStatus.DEPRECATED:
            return deprecated()
