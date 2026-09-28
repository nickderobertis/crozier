

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .rate_limit_algorithm import RateLimitAlgorithm


class RateLimit(UniversalBaseModel):
    """
    declarative protocol-agnostic rate limit / quota
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Shared counter key; expectations with the same name share one rate-limit counter. When omitted the expectation id is used as the key
    """

    algorithm: typing.Optional[RateLimitAlgorithm] = pydantic.Field(default=None)
    """
    Rate-limiting algorithm; defaults to fixed_window
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    fixed_window: maximum requests allowed per window before requests are rejected
    """

    window_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="windowMillis"),
        pydantic.Field(alias="windowMillis", description="fixed_window: fixed-window length in milliseconds"),
    ] = None
    """
    fixed_window: fixed-window length in milliseconds
    """

    burst: typing.Optional[int] = pydantic.Field(default=None)
    """
    token_bucket: bucket capacity in tokens
    """

    refill_per_second: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="refillPerSecond"),
        pydantic.Field(alias="refillPerSecond", description="token_bucket: token refill rate per second"),
    ] = None
    """
    token_bucket: token refill rate per second
    """

    error_status: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="errorStatus"),
        pydantic.Field(alias="errorStatus", description="Status returned when the request is over-limit (default 429)"),
    ] = None
    """
    Status returned when the request is over-limit (default 429)
    """

    retry_after: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="retryAfter"),
        pydantic.Field(
            alias="retryAfter",
            description="Literal Retry-After header value; when omitted it is computed from the window/bucket reset time",
        ),
    ] = None
    """
    Literal Retry-After header value; when omitted it is computed from the window/bucket reset time
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
