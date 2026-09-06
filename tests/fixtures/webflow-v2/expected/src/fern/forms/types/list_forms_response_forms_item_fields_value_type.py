

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListFormsResponseFormsItemFieldsValueType(enum.StrEnum):
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
        if self is ListFormsResponseFormsItemFieldsValueType.PLAIN:
            return plain()
        if self is ListFormsResponseFormsItemFieldsValueType.EMAIL:
            return email()
        if self is ListFormsResponseFormsItemFieldsValueType.PASSWORD:
            return password()
        if self is ListFormsResponseFormsItemFieldsValueType.PHONE:
            return phone()
        if self is ListFormsResponseFormsItemFieldsValueType.NUMBER:
            return number()
