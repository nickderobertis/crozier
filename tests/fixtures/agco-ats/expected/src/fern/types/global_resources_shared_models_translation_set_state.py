

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GlobalResourcesSharedModelsTranslationSetState(enum.StrEnum):
    """
    An enum indicating the state of the translation set
    """

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
        if self is GlobalResourcesSharedModelsTranslationSetState.OUT_FOR_PROCESSING:
            return out_for_processing()
        if self is GlobalResourcesSharedModelsTranslationSetState.PROCESSING:
            return processing()
        if self is GlobalResourcesSharedModelsTranslationSetState.PENDING_APPROVAL:
            return pending_approval()
        if self is GlobalResourcesSharedModelsTranslationSetState.OUT_FOR_TRANSLATION:
            return out_for_translation()
        if self is GlobalResourcesSharedModelsTranslationSetState.CANCELLED:
            return cancelled()
        if self is GlobalResourcesSharedModelsTranslationSetState.COMPLETED:
            return completed()
