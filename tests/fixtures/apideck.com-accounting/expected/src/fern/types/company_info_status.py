

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CompanyInfoStatus(str, enum.Enum):
    """
    Based on the status some functionality is enabled or disabled.
    """

    ACTIVE = "active"
    INACTIVE = "inactive"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is CompanyInfoStatus.ACTIVE:
            return active()
        if self is CompanyInfoStatus.INACTIVE:
            return inactive()
