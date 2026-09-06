

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TranslationSetsGetTranslationSetsRequestState(enum.StrEnum):
    OUT_FOR_PROCESSING = "OutForProcessing"
    PROCESSING = "Processing"
    PENDING_APPROVAL = "PendingApproval"
    OUT_FOR_TRANSLATION = "OutForTranslation"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"

    def visit(
        self,
        out_for_processing: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        pending_approval: typing.Callable[[], T_Result],
        out_for_translation: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TranslationSetsGetTranslationSetsRequestState.OUT_FOR_PROCESSING:
            return out_for_processing()
        if self is TranslationSetsGetTranslationSetsRequestState.PROCESSING:
            return processing()
        if self is TranslationSetsGetTranslationSetsRequestState.PENDING_APPROVAL:
            return pending_approval()
        if self is TranslationSetsGetTranslationSetsRequestState.OUT_FOR_TRANSLATION:
            return out_for_translation()
        if self is TranslationSetsGetTranslationSetsRequestState.CANCELLED:
            return cancelled()
        if self is TranslationSetsGetTranslationSetsRequestState.COMPLETED:
            return completed()
