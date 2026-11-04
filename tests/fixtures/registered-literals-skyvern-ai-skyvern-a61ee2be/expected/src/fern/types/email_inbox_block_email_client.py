

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmailInboxBlockEmailClient(enum.StrEnum):
    GMAIL = "gmail"
    OUTLOOK = "outlook"

    def visit(self, gmail: typing.Callable[[], T_Result], outlook: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmailInboxBlockEmailClient.GMAIL:
            return gmail()
        if self is EmailInboxBlockEmailClient.OUTLOOK:
            return outlook()
