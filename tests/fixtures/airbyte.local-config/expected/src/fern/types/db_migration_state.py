

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DbMigrationState(str, enum.Enum):
    PENDING = "pending"
    ABOVE_TARGET = "above_target"
    BELOW_BASELINE = "below_baseline"
    BASELINE = "baseline"
    IGNORED = "ignored"
    MISSING_SUCCESS = "missing_success"
    MISSING_FAILED = "missing_failed"
    SUCCESS = "success"
    UNDONE = "undone"
    AVAILABLE = "available"
    FAILED = "failed"
    OUT_OF_ORDER = "out_of_order"
    FUTURE_SUCCESS = "future_success"
    FUTURE_FAILED = "future_failed"
    OUTDATED = "outdated"
    SUPERSEDED = "superseded"
    DELETED = "deleted"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        above_target: typing.Callable[[], T_Result],
        below_baseline: typing.Callable[[], T_Result],
        baseline: typing.Callable[[], T_Result],
        ignored: typing.Callable[[], T_Result],
        missing_success: typing.Callable[[], T_Result],
        missing_failed: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        undone: typing.Callable[[], T_Result],
        available: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        out_of_order: typing.Callable[[], T_Result],
        future_success: typing.Callable[[], T_Result],
        future_failed: typing.Callable[[], T_Result],
        outdated: typing.Callable[[], T_Result],
        superseded: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DbMigrationState.PENDING:
            return pending()
        if self is DbMigrationState.ABOVE_TARGET:
            return above_target()
        if self is DbMigrationState.BELOW_BASELINE:
            return below_baseline()
        if self is DbMigrationState.BASELINE:
            return baseline()
        if self is DbMigrationState.IGNORED:
            return ignored()
        if self is DbMigrationState.MISSING_SUCCESS:
            return missing_success()
        if self is DbMigrationState.MISSING_FAILED:
            return missing_failed()
        if self is DbMigrationState.SUCCESS:
            return success()
        if self is DbMigrationState.UNDONE:
            return undone()
        if self is DbMigrationState.AVAILABLE:
            return available()
        if self is DbMigrationState.FAILED:
            return failed()
        if self is DbMigrationState.OUT_OF_ORDER:
            return out_of_order()
        if self is DbMigrationState.FUTURE_SUCCESS:
            return future_success()
        if self is DbMigrationState.FUTURE_FAILED:
            return future_failed()
        if self is DbMigrationState.OUTDATED:
            return outdated()
        if self is DbMigrationState.SUPERSEDED:
            return superseded()
        if self is DbMigrationState.DELETED:
            return deleted()
