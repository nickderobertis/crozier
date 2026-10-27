

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateChatRequestChatType(enum.StrEnum):
    ONE_ON_ONE = "oneOnOne"
    GROUP = "group"
    MEETING = "meeting"

    def visit(
        self,
        one_on_one: typing.Callable[[], T_Result],
        group: typing.Callable[[], T_Result],
        meeting: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateChatRequestChatType.ONE_ON_ONE:
            return one_on_one()
        if self is CreateChatRequestChatType.GROUP:
            return group()
        if self is CreateChatRequestChatType.MEETING:
            return meeting()
