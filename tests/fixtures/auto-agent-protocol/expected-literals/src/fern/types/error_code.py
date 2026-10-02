

import typing

ErrorCode = typing.Union[
    typing.Literal[
        "UNSUPPORTED_SKILL",
        "SCHEMA_VALIDATION_FAILED",
        "MISSING_REQUIRED_FIELD",
        "INVALID_CONDITION",
        "VEHICLE_NOT_FOUND",
        "VEHICLE_UNAVAILABLE",
        "CONTACT_CONSENT_REQUIRED",
        "INVALID_CONSENT",
        "APPOINTMENT_TIME_UNAVAILABLE",
        "IDEMPOTENCY_CONFLICT",
        "RATE_LIMITED",
        "INTERNAL_ERROR",
    ],
    typing.Any,
]
