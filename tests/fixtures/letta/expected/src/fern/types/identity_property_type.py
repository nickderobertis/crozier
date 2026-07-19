

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdentityPropertyType(enum.StrEnum):
    """
    Enum to represent the type of the identity property.
    """

    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    JSON = "json"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentityPropertyType.STRING:
            return string()
        if self is IdentityPropertyType.NUMBER:
            return number()
        if self is IdentityPropertyType.BOOLEAN:
            return boolean()
        if self is IdentityPropertyType.JSON:
            return json()
