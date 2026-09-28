

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateProcareMessageRequestType(enum.StrEnum):
    """
    Case-insensitive; surrounding whitespace is ignored.
    """

    OFFICE_CHAT = "office_chat"
    CLASSROOM_CHAT = "classroom_chat"

    def visit(
        self, office_chat: typing.Callable[[], T_Result], classroom_chat: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is CreateProcareMessageRequestType.OFFICE_CHAT:
            return office_chat()
        if self is CreateProcareMessageRequestType.CLASSROOM_CHAT:
            return classroom_chat()
