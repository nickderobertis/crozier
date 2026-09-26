

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IvcsWebhookType(enum.StrEnum):
    VCS_WEBHOOK = "VCSWebhook"

    def visit(self, vcs_webhook: typing.Callable[[], T_Result]) -> T_Result:
        if self is IvcsWebhookType.VCS_WEBHOOK:
            return vcs_webhook()
