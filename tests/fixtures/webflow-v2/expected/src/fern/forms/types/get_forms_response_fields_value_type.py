

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFormsResponseFieldsValueType(enum.StrEnum):
    """
    The field type
    """

    PLAIN = "Plain"
    EMAIL = "Email"
    PASSWORD = "Password"
    PHONE = "Phone"
    NUMBER = "Number"

    def visit(
        self,
        plain: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        password: typing.Callable[[], T_Result],
        phone: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetFormsResponseFieldsValueType.PLAIN:
            return plain()
        if self is GetFormsResponseFieldsValueType.EMAIL:
            return email()
        if self is GetFormsResponseFieldsValueType.PASSWORD:
            return password()
        if self is GetFormsResponseFieldsValueType.PHONE:
            return phone()
        if self is GetFormsResponseFieldsValueType.NUMBER:
            return number()
