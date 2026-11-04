

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SchemaResponseActionReadResponseAttributesToState(enum.StrEnum):
    """
    The name of the state of the Schema Response after the creation of the action
    """

    IN_PROGRESS = "in_progress"
    APPROVED = "approved"
    PENDING_MODERATION = "pending_moderation"

    def visit(
        self,
        in_progress: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        pending_moderation: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SchemaResponseActionReadResponseAttributesToState.IN_PROGRESS:
            return in_progress()
        if self is SchemaResponseActionReadResponseAttributesToState.APPROVED:
            return approved()
        if self is SchemaResponseActionReadResponseAttributesToState.PENDING_MODERATION:
            return pending_moderation()
