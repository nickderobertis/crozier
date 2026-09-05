

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostGetStatusRequestVersion(enum.StrEnum):
    TWO_THOUSAND_TEN0601 = "2010-06-01"

    def visit(self, two_thousand_ten0601: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostGetStatusRequestVersion.TWO_THOUSAND_TEN0601:
            return two_thousand_ten0601()
