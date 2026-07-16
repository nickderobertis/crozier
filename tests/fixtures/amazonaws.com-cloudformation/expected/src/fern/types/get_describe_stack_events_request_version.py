

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetDescribeStackEventsRequestVersion(str, enum.Enum):
    TWO_THOUSAND_TEN0515 = "2010-05-15"

    def visit(self, two_thousand_ten0515: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribeStackEventsRequestVersion.TWO_THOUSAND_TEN0515:
            return two_thousand_ten0515()
