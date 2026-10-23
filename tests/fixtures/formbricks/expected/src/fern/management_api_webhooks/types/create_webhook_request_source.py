

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateWebhookRequestSource(enum.StrEnum):
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
        if self is CreateWebhookRequestSource.USER:
            return user()
        if self is CreateWebhookRequestSource.ZAPIER:
            return zapier()
        if self is CreateWebhookRequestSource.MAKE:
            return make()
        if self is CreateWebhookRequestSource.N8N:
            return n8n()
