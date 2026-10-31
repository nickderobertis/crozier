

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HandleVcsWebhookRequestProvider(enum.StrEnum):
    GITHUB = "github"

    def visit(self, github: typing.Callable[[], T_Result]) -> T_Result:
        if self is HandleVcsWebhookRequestProvider.GITHUB:
            return github()
