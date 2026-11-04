

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookListMatchingScopeRequestScopeType(enum.StrEnum):
    PROJECT = "project"

    def visit(self, project: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebhookListMatchingScopeRequestScopeType.PROJECT:
            return project()
