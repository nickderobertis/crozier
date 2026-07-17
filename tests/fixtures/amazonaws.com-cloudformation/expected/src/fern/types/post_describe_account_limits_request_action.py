

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDescribeAccountLimitsRequestAction(enum.StrEnum):
    DESCRIBE_ACCOUNT_LIMITS = "DescribeAccountLimits"

    def visit(self, describe_account_limits: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeAccountLimitsRequestAction.DESCRIBE_ACCOUNT_LIMITS:
            return describe_account_limits()
