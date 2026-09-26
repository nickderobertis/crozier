

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_code import ErrorCode
from .error_type import ErrorType


class Error(UniversalBaseModel):
    """
    Typed AAP error payload. Returned inside an A2A error envelope (JSON-RPC 'error' member or HTTP 'application/json' error body, per A2A spec sections 9.5 and 11.6). Buyer agents use 'code' and 'retryable' to drive client behavior; humans see 'message'.
    """

    type: ErrorType
    error_id: str = pydantic.Field()
    """
    Unique identifier for this error instance, suitable for support correlation (e.g. UUID).
    """

    code: ErrorCode = pydantic.Field()
    """
    Machine-readable error code from the AAP error vocabulary.
    """

    message: str = pydantic.Field()
    """
    Human-readable error message suitable for end-user display.
    """

    retryable: bool = pydantic.Field()
    """
    Whether the buyer agent SHOULD retry the same request after a backoff.
    """

    details: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Optional, code-specific details (e.g. validation failure paths). Free shape.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    ISO 8601 / RFC 3339 timestamp at which the dealer agent generated this error (e.g. '2026-04-30T10:15:30Z'). MUST include a timezone offset (Z or ±HH:MM).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
