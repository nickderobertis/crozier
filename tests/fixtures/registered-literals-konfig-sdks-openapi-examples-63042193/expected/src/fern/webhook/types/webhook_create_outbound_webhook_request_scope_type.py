

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookCreateOutboundWebhookRequestScopeType(enum.StrEnum):
    """
    Type of the scope being used
    """

    PROJECT = "project"

    def visit(self, project: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebhookCreateOutboundWebhookRequestScopeType.PROJECT:
            return project()
