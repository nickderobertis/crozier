

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FilterCapabilityType(enum.StrEnum):
    """
    The filter's value type. `date` values are ISO 8601 strings. `boolean` values are the strings `"true"` and `"false"`.
    """

    STRING = "string"
    DATE = "date"
    NUMBER = "number"
    BOOLEAN = "boolean"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FilterCapabilityType.STRING:
            return string()
        if self is FilterCapabilityType.DATE:
            return date()
        if self is FilterCapabilityType.NUMBER:
            return number()
        if self is FilterCapabilityType.BOOLEAN:
            return boolean()
