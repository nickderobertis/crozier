

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDescribeTypeRegistrationRequestAction(enum.StrEnum):
    DESCRIBE_TYPE_REGISTRATION = "DescribeTypeRegistration"

    def visit(self, describe_type_registration: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeTypeRegistrationRequestAction.DESCRIBE_TYPE_REGISTRATION:
            return describe_type_registration()
