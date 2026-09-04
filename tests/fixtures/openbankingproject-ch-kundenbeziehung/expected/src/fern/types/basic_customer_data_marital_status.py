

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BasicCustomerDataMaritalStatus(enum.StrEnum):
    SINGLE = "single"
    MARRIED = "married"
    DIVORCED = "divorced"
    WIDOWED = "widowed"
    REGISTERED_PARTNERSHIP = "registered_partnership"

    def visit(
        self,
        single: typing.Callable[[], T_Result],
        married: typing.Callable[[], T_Result],
        divorced: typing.Callable[[], T_Result],
        widowed: typing.Callable[[], T_Result],
        registered_partnership: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BasicCustomerDataMaritalStatus.SINGLE:
            return single()
        if self is BasicCustomerDataMaritalStatus.MARRIED:
            return married()
        if self is BasicCustomerDataMaritalStatus.DIVORCED:
            return divorced()
        if self is BasicCustomerDataMaritalStatus.WIDOWED:
            return widowed()
        if self is BasicCustomerDataMaritalStatus.REGISTERED_PARTNERSHIP:
            return registered_partnership()
