

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookSupportManagedVia(enum.StrEnum):
    """
    How the subscription is managed in the downstream.
    """

    MANUAL = "manual"
    API = "api"

    def visit(self, manual: typing.Callable[[], T_Result], api: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebhookSupportManagedVia.MANUAL:
            return manual()
        if self is WebhookSupportManagedVia.API:
            return api()
