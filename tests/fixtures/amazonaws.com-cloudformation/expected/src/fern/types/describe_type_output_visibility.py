

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DescribeTypeOutputVisibility(enum.StrEnum):
    """
    <p>The scope at which the extension is visible and usable in CloudFormation operations.</p> <p>Valid values include:</p> <ul> <li> <p> <code>PRIVATE</code>: The extension is only visible and usable within the account in which it is registered. CloudFormation marks any extensions you register as <code>PRIVATE</code>.</p> </li> <li> <p> <code>PUBLIC</code>: The extension is publicly visible and usable within any Amazon Web Services account.</p> </li> </ul>
    """

    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"

    def visit(self, public: typing.Callable[[], T_Result], private: typing.Callable[[], T_Result]) -> T_Result:
        if self is DescribeTypeOutputVisibility.PUBLIC:
            return public()
        if self is DescribeTypeOutputVisibility.PRIVATE:
            return private()
