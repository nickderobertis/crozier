

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListTypesInputDeprecatedStatus(enum.StrEnum):
    """
    <p>The deprecation status of the extension that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension is registered for use in CloudFormation operations.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul>
    """

    LIVE = "LIVE"
    DEPRECATED = "DEPRECATED"

    def visit(self, live: typing.Callable[[], T_Result], deprecated: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListTypesInputDeprecatedStatus.LIVE:
            return live()
        if self is ListTypesInputDeprecatedStatus.DEPRECATED:
            return deprecated()
