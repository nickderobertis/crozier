

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorCode(enum.StrEnum):
    """
    Machine-readable error code from the AAP error vocabulary.
    """

    UNSUPPORTED_SKILL = "UNSUPPORTED_SKILL"
    SCHEMA_VALIDATION_FAILED = "SCHEMA_VALIDATION_FAILED"
    MISSING_REQUIRED_FIELD = "MISSING_REQUIRED_FIELD"
    INVALID_CONDITION = "INVALID_CONDITION"
    VEHICLE_NOT_FOUND = "VEHICLE_NOT_FOUND"
    VEHICLE_UNAVAILABLE = "VEHICLE_UNAVAILABLE"
    CONTACT_CONSENT_REQUIRED = "CONTACT_CONSENT_REQUIRED"
    INVALID_CONSENT = "INVALID_CONSENT"
    APPOINTMENT_TIME_UNAVAILABLE = "APPOINTMENT_TIME_UNAVAILABLE"
    IDEMPOTENCY_CONFLICT = "IDEMPOTENCY_CONFLICT"
    RATE_LIMITED = "RATE_LIMITED"
    INTERNAL_ERROR = "INTERNAL_ERROR"

    def visit(
        self,
        unsupported_skill: typing.Callable[[], T_Result],
        schema_validation_failed: typing.Callable[[], T_Result],
        missing_required_field: typing.Callable[[], T_Result],
        invalid_condition: typing.Callable[[], T_Result],
        vehicle_not_found: typing.Callable[[], T_Result],
        vehicle_unavailable: typing.Callable[[], T_Result],
        contact_consent_required: typing.Callable[[], T_Result],
        invalid_consent: typing.Callable[[], T_Result],
        appointment_time_unavailable: typing.Callable[[], T_Result],
        idempotency_conflict: typing.Callable[[], T_Result],
        rate_limited: typing.Callable[[], T_Result],
        internal_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ErrorCode.UNSUPPORTED_SKILL:
            return unsupported_skill()
        if self is ErrorCode.SCHEMA_VALIDATION_FAILED:
            return schema_validation_failed()
        if self is ErrorCode.MISSING_REQUIRED_FIELD:
            return missing_required_field()
        if self is ErrorCode.INVALID_CONDITION:
            return invalid_condition()
        if self is ErrorCode.VEHICLE_NOT_FOUND:
            return vehicle_not_found()
        if self is ErrorCode.VEHICLE_UNAVAILABLE:
            return vehicle_unavailable()
        if self is ErrorCode.CONTACT_CONSENT_REQUIRED:
            return contact_consent_required()
        if self is ErrorCode.INVALID_CONSENT:
            return invalid_consent()
        if self is ErrorCode.APPOINTMENT_TIME_UNAVAILABLE:
            return appointment_time_unavailable()
        if self is ErrorCode.IDEMPOTENCY_CONFLICT:
            return idempotency_conflict()
        if self is ErrorCode.RATE_LIMITED:
            return rate_limited()
        if self is ErrorCode.INTERNAL_ERROR:
            return internal_error()
