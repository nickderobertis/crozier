

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateWebhookResponseSource(enum.StrEnum):
    """
    The source of the webhook
    """

    USER = "user"
    ZAPIER = "zapier"
    MAKE = "make"
    N8N = "n8n"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        zapier: typing.Callable[[], T_Result],
        make: typing.Callable[[], T_Result],
        n8n: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateWebhookResponseSource.USER:
            return user()
        if self is CreateWebhookResponseSource.ZAPIER:
            return zapier()
        if self is CreateWebhookResponseSource.MAKE:
            return make()
        if self is CreateWebhookResponseSource.N8N:
            return n8n()
