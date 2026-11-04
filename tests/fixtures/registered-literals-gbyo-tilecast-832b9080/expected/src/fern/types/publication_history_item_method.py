

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PublicationHistoryItemMethod(enum.StrEnum):
    MANUAL = "manual"
    AUTOMATIC_AFTER_APPROVAL = "automatic_after_approval"
    SCHEDULED = "scheduled"
    ROLLBACK = "rollback"
    MIGRATION = "migration"
    BACKFILL = "backfill"

    def visit(
        self,
        manual: typing.Callable[[], T_Result],
        automatic_after_approval: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        rollback: typing.Callable[[], T_Result],
        migration: typing.Callable[[], T_Result],
        backfill: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PublicationHistoryItemMethod.MANUAL:
            return manual()
        if self is PublicationHistoryItemMethod.AUTOMATIC_AFTER_APPROVAL:
            return automatic_after_approval()
        if self is PublicationHistoryItemMethod.SCHEDULED:
            return scheduled()
        if self is PublicationHistoryItemMethod.ROLLBACK:
            return rollback()
        if self is PublicationHistoryItemMethod.MIGRATION:
            return migration()
        if self is PublicationHistoryItemMethod.BACKFILL:
            return backfill()
