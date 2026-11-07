

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SchemaResponsePpostResponseAttributesReviewsState(enum.StrEnum):
    """
    A string that represents Schema Response state. `initial` is the state of a Schema Response on a newly registered Registration, to edit a Schema Response you must create a Schema Response Action that triggers a new submission.
    """

    INITIAL = "initial"
    IN_PROGRESS = "in_progress"
    APPROVED = "approved"
    PENDING_MODERATION = "pending_moderation"

    def visit(
        self,
        initial: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        pending_moderation: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SchemaResponsePpostResponseAttributesReviewsState.INITIAL:
            return initial()
        if self is SchemaResponsePpostResponseAttributesReviewsState.IN_PROGRESS:
            return in_progress()
        if self is SchemaResponsePpostResponseAttributesReviewsState.APPROVED:
            return approved()
        if self is SchemaResponsePpostResponseAttributesReviewsState.PENDING_MODERATION:
            return pending_moderation()
