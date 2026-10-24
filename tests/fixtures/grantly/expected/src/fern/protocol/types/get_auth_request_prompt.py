

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAuthRequestPrompt(enum.StrEnum):
    CONSENT = "consent"

    def visit(self, consent: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetAuthRequestPrompt.CONSENT:
            return consent()
