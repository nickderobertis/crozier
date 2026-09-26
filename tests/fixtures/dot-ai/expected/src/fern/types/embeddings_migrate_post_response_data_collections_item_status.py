

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmbeddingsMigratePostResponseDataCollectionsItemStatus(enum.StrEnum):
    """
    Migration outcome
    """

    MIGRATED = "migrated"
    SKIPPED = "skipped"
    FAILED = "failed"

    def visit(
        self,
        migrated: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmbeddingsMigratePostResponseDataCollectionsItemStatus.MIGRATED:
            return migrated()
        if self is EmbeddingsMigratePostResponseDataCollectionsItemStatus.SKIPPED:
            return skipped()
        if self is EmbeddingsMigratePostResponseDataCollectionsItemStatus.FAILED:
            return failed()
