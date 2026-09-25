

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VCardMessageType(enum.StrEnum):
    """
    The type of message to send. You must provide `vcard` in this field
    """

    VCARD = "vcard"

    def visit(self, vcard: typing.Callable[[], T_Result]) -> T_Result:
        if self is VCardMessageType.VCARD:
            return vcard()
