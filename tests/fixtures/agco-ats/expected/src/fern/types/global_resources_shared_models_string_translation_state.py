

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GlobalResourcesSharedModelsStringTranslationState(enum.StrEnum):
    """
    The state of the translation
    """

    ORIGINAL = "Original"
    REQUESTED = "Requested"
    PROCESSING = "Processing"
    PROCESSED = "Processed"
    VALIDATED = "Validated"
    INVALIDATED = "Invalidated"
    REQUEST_PENDING = "RequestPending"
    CREATE_PENDING = "CreatePending"

    def visit(
        self,
        original: typing.Callable[[], T_Result],
        requested: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        processed: typing.Callable[[], T_Result],
        validated: typing.Callable[[], T_Result],
        invalidated: typing.Callable[[], T_Result],
        request_pending: typing.Callable[[], T_Result],
        create_pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GlobalResourcesSharedModelsStringTranslationState.ORIGINAL:
            return original()
        if self is GlobalResourcesSharedModelsStringTranslationState.REQUESTED:
            return requested()
        if self is GlobalResourcesSharedModelsStringTranslationState.PROCESSING:
            return processing()
        if self is GlobalResourcesSharedModelsStringTranslationState.PROCESSED:
            return processed()
        if self is GlobalResourcesSharedModelsStringTranslationState.VALIDATED:
            return validated()
        if self is GlobalResourcesSharedModelsStringTranslationState.INVALIDATED:
            return invalidated()
        if self is GlobalResourcesSharedModelsStringTranslationState.REQUEST_PENDING:
            return request_pending()
        if self is GlobalResourcesSharedModelsStringTranslationState.CREATE_PENDING:
            return create_pending()
