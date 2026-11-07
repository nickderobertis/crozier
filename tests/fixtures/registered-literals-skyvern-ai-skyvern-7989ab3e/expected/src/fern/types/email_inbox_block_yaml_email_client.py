

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmailInboxBlockYamlEmailClient(enum.StrEnum):
    GMAIL = "gmail"
    OUTLOOK = "outlook"

    def visit(self, gmail: typing.Callable[[], T_Result], outlook: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmailInboxBlockYamlEmailClient.GMAIL:
            return gmail()
        if self is EmailInboxBlockYamlEmailClient.OUTLOOK:
            return outlook()
