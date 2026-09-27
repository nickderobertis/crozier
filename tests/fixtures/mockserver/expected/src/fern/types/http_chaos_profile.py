

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay import Delay


class HttpChaosProfile(UniversalBaseModel):
    """
    chaos profile controlling fault injection for a host or expectation
    """

    error_status: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="errorStatus"),
        pydantic.Field(
            alias="errorStatus", description="HTTP error status code to return instead of the real response"
        ),
    ] = None
    """
    HTTP error status code to return instead of the real response
    """

    error_probability: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="errorProbability"),
        pydantic.Field(
            alias="errorProbability", description="probability (0.0 to 1.0) that a request triggers the error"
        ),
    ] = None
    """
    probability (0.0 to 1.0) that a request triggers the error
    """

    latency: typing.Optional[Delay] = None
    seed: typing.Optional[int] = pydantic.Field(default=None)
    """
    fixed seed for deterministic probabilistic outcomes
    """

    retry_after: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="retryAfter"), pydantic.Field(alias="retryAfter")
    ] = None
    drop_connection_probability: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="dropConnectionProbability"),
        pydantic.Field(
            alias="dropConnectionProbability",
            description="Probability (0.0 to 1.0) of dropping the TCP connection without sending any response",
        ),
    ] = None
    """
    Probability (0.0 to 1.0) of dropping the TCP connection without sending any response
    """

    succeed_first: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="succeedFirst"), pydantic.Field(alias="succeedFirst")
    ] = None
    fail_request_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="failRequestCount"), pydantic.Field(alias="failRequestCount")
    ] = None
    outage_after_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="outageAfterMillis"),
        pydantic.Field(
            alias="outageAfterMillis",
            description="Time-based outage window: chaos becomes active this many milliseconds after the expectation's first match (measured via the controllable clock)",
        ),
    ] = None
    """
    Time-based outage window: chaos becomes active this many milliseconds after the expectation's first match (measured via the controllable clock)
    """

    outage_duration_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="outageDurationMillis"),
        pydantic.Field(
            alias="outageDurationMillis",
            description="Time-based outage window: chaos stays active for this many milliseconds then self-heals; omit for an unbounded outage",
        ),
    ] = None
    """
    Time-based outage window: chaos stays active for this many milliseconds then self-heals; omit for an unbounded outage
    """

    truncate_body_at_fraction: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="truncateBodyAtFraction"),
        pydantic.Field(
            alias="truncateBodyAtFraction",
            description="Corrupt the response body by keeping only this leading fraction (0.0 to 1.0) of its bytes",
        ),
    ] = None
    """
    Corrupt the response body by keeping only this leading fraction (0.0 to 1.0) of its bytes
    """

    malformed_body: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="malformedBody"),
        pydantic.Field(
            alias="malformedBody",
            description="Corrupt the response body by appending a broken-JSON fragment so it fails to parse",
        ),
    ] = None
    """
    Corrupt the response body by appending a broken-JSON fragment so it fails to parse
    """

    slow_response_chunk_size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="slowResponseChunkSize"),
        pydantic.Field(
            alias="slowResponseChunkSize",
            description="Dribble the response body in chunks of this many bytes; requires slowResponseChunkDelay to slow the response",
        ),
    ] = None
    """
    Dribble the response body in chunks of this many bytes; requires slowResponseChunkDelay to slow the response
    """

    slow_response_chunk_delay: typing_extensions.Annotated[
        typing.Optional[Delay],
        FieldMetadata(alias="slowResponseChunkDelay"),
        pydantic.Field(alias="slowResponseChunkDelay"),
    ] = None
    quota_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="quotaName"),
        pydantic.Field(
            alias="quotaName",
            description="Stateful quota: shared counter key; expectations with the same quotaName share one rate-limit counter",
        ),
    ] = None
    """
    Stateful quota: shared counter key; expectations with the same quotaName share one rate-limit counter
    """

    quota_limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="quotaLimit"),
        pydantic.Field(
            alias="quotaLimit",
            description="Stateful quota: max requests allowed per window before requests are rejected",
        ),
    ] = None
    """
    Stateful quota: max requests allowed per window before requests are rejected
    """

    quota_window_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="quotaWindowMillis"),
        pydantic.Field(alias="quotaWindowMillis", description="Stateful quota: fixed-window length in milliseconds"),
    ] = None
    """
    Stateful quota: fixed-window length in milliseconds
    """

    quota_error_status: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="quotaErrorStatus"),
        pydantic.Field(
            alias="quotaErrorStatus",
            description="Stateful quota: status returned when the quota is exceeded (default 429)",
        ),
    ] = None
    """
    Stateful quota: status returned when the quota is exceeded (default 429)
    """

    degradation_ramp_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="degradationRampMillis"),
        pydantic.Field(
            alias="degradationRampMillis",
            description="Gradual degradation: ramp errorProbability and dropConnectionProbability linearly from 0 to their configured values over this many milliseconds from the first match",
        ),
    ] = None
    """
    Gradual degradation: ramp errorProbability and dropConnectionProbability linearly from 0 to their configured values over this many milliseconds from the first match
    """

    graphql_errors: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="graphqlErrors"),
        pydantic.Field(alias="graphqlErrors", description="Replace the response body with a GraphQL errors envelope"),
    ] = None
    """
    Replace the response body with a GraphQL errors envelope
    """

    graphql_error_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="graphqlErrorMessage"),
        pydantic.Field(
            alias="graphqlErrorMessage", description="Message text used in the injected GraphQL error entry"
        ),
    ] = None
    """
    Message text used in the injected GraphQL error entry
    """

    graphql_error_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="graphqlErrorCode"),
        pydantic.Field(
            alias="graphqlErrorCode", description="Value of extensions.code in the injected GraphQL error entry"
        ),
    ] = None
    """
    Value of extensions.code in the injected GraphQL error entry
    """

    graphql_nullify_data: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="graphqlNullifyData"),
        pydantic.Field(
            alias="graphqlNullifyData",
            description="Set the GraphQL response 'data' member to null alongside the injected errors",
        ),
    ] = None
    """
    Set the GraphQL response 'data' member to null alongside the injected errors
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
