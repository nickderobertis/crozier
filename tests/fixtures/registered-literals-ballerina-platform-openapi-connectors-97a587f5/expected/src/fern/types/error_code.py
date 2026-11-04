

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorCode(enum.StrEnum):
    """
    Error codes as defined in the Microsoft REST guidelines
    (https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses).
    """

    CONFLICT = "conflict"
    INVALID_PAYLOAD = "invalidPayload"
    FORBIDDEN = "forbidden"
    NOT_FOUND = "notFound"
    UNEXPECTED_ENTITY_STATE = "unexpectedEntityState"
    ITEM_DOES_ALREADY_EXIST = "itemDoesAlreadyExist"
    SERVICE_UNAVAILABLE = "serviceUnavailable"
    INTERNAL_FAILURE = "internalFailure"
    QUOTA_EXCEEDED = "quotaExceeded"
    JSONL_VALIDATION_FAILED = "jsonlValidationFailed"
    FILE_IMPORT_FAILED = "fileImportFailed"

    def visit(
        self,
        conflict: typing.Callable[[], T_Result],
        invalid_payload: typing.Callable[[], T_Result],
        forbidden: typing.Callable[[], T_Result],
        not_found: typing.Callable[[], T_Result],
        unexpected_entity_state: typing.Callable[[], T_Result],
        item_does_already_exist: typing.Callable[[], T_Result],
        service_unavailable: typing.Callable[[], T_Result],
        internal_failure: typing.Callable[[], T_Result],
        quota_exceeded: typing.Callable[[], T_Result],
        jsonl_validation_failed: typing.Callable[[], T_Result],
        file_import_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ErrorCode.CONFLICT:
            return conflict()
        if self is ErrorCode.INVALID_PAYLOAD:
            return invalid_payload()
        if self is ErrorCode.FORBIDDEN:
            return forbidden()
        if self is ErrorCode.NOT_FOUND:
            return not_found()
        if self is ErrorCode.UNEXPECTED_ENTITY_STATE:
            return unexpected_entity_state()
        if self is ErrorCode.ITEM_DOES_ALREADY_EXIST:
            return item_does_already_exist()
        if self is ErrorCode.SERVICE_UNAVAILABLE:
            return service_unavailable()
        if self is ErrorCode.INTERNAL_FAILURE:
            return internal_failure()
        if self is ErrorCode.QUOTA_EXCEEDED:
            return quota_exceeded()
        if self is ErrorCode.JSONL_VALIDATION_FAILED:
            return jsonl_validation_failed()
        if self is ErrorCode.FILE_IMPORT_FAILED:
            return file_import_failed()
