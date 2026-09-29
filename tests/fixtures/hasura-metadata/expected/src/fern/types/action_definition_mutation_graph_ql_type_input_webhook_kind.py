

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionDefinitionMutationGraphQlTypeInputWebhookKind(enum.StrEnum):
    SYNCHRONOUS = "synchronous"
    ASYNCHRONOUS = "asynchronous"

    def visit(
        self, synchronous: typing.Callable[[], T_Result], asynchronous: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ActionDefinitionMutationGraphQlTypeInputWebhookKind.SYNCHRONOUS:
            return synchronous()
        if self is ActionDefinitionMutationGraphQlTypeInputWebhookKind.ASYNCHRONOUS:
            return asynchronous()
