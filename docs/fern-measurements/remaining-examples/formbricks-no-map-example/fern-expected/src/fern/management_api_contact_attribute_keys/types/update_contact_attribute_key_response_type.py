

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateContactAttributeKeyResponseType(enum.StrEnum):
    """
    Whether this is a default or custom attribute
    """

    DEFAULT = "default"
    CUSTOM = "custom"

    def visit(self, default: typing.Callable[[], T_Result], custom: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateContactAttributeKeyResponseType.DEFAULT:
            return default()
        if self is UpdateContactAttributeKeyResponseType.CUSTOM:
            return custom()
