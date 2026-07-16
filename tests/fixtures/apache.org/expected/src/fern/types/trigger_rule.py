

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TriggerRule(enum.StrEnum):
    """
    Trigger rule.

    *Changed in version 2.2.0*&#58; 'none_failed_min_one_success' is added as a possible value.
    """

    ALL_SUCCESS = "all_success"
    ALL_FAILED = "all_failed"
    ALL_DONE = "all_done"
    ONE_SUCCESS = "one_success"
    ONE_FAILED = "one_failed"
    NONE_FAILED = "none_failed"
    NONE_SKIPPED = "none_skipped"
    NONE_FAILED_OR_SKIPPED = "none_failed_or_skipped"
    NONE_FAILED_MIN_ONE_SUCCESS = "none_failed_min_one_success"
    DUMMY = "dummy"

    def visit(
        self,
        all_success: typing.Callable[[], T_Result],
        all_failed: typing.Callable[[], T_Result],
        all_done: typing.Callable[[], T_Result],
        one_success: typing.Callable[[], T_Result],
        one_failed: typing.Callable[[], T_Result],
        none_failed: typing.Callable[[], T_Result],
        none_skipped: typing.Callable[[], T_Result],
        none_failed_or_skipped: typing.Callable[[], T_Result],
        none_failed_min_one_success: typing.Callable[[], T_Result],
        dummy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TriggerRule.ALL_SUCCESS:
            return all_success()
        if self is TriggerRule.ALL_FAILED:
            return all_failed()
        if self is TriggerRule.ALL_DONE:
            return all_done()
        if self is TriggerRule.ONE_SUCCESS:
            return one_success()
        if self is TriggerRule.ONE_FAILED:
            return one_failed()
        if self is TriggerRule.NONE_FAILED:
            return none_failed()
        if self is TriggerRule.NONE_SKIPPED:
            return none_skipped()
        if self is TriggerRule.NONE_FAILED_OR_SKIPPED:
            return none_failed_or_skipped()
        if self is TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS:
            return none_failed_min_one_success()
        if self is TriggerRule.DUMMY:
            return dummy()
