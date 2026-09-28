

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2enrichment_provider_outcome import V2EnrichmentProviderOutcome


class V2EnrichmentRunDetail(UniversalBaseModel):
    """
    Provider cascade, cost, and timing for one enrichment cell.
    """

    started_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="startedAt"),
        pydantic.Field(
            alias="startedAt", description="ISO 8601 timestamp when the cascade started, or null when not recorded."
        ),
    ] = None
    """
    ISO 8601 timestamp when the cascade started, or null when not recorded.
    """

    completed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="completedAt"),
        pydantic.Field(
            alias="completedAt", description="ISO 8601 timestamp when the cascade finished, or null when not recorded."
        ),
    ] = None
    """
    ISO 8601 timestamp when the cascade finished, or null when not recorded.
    """

    duration_ms: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="durationMs"),
        pydantic.Field(
            alias="durationMs", description="Wall-clock milliseconds across the whole cascade; zero when not recorded."
        ),
    ]
    """
    Wall-clock milliseconds across the whole cascade; zero when not recorded.
    """

    total_cost: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="totalCost"),
        pydantic.Field(
            alias="totalCost", description="Sum of per-provider hosted-key cost in USD; zero when not recorded."
        ),
    ]
    """
    Sum of per-provider hosted-key cost in USD; zero when not recorded.
    """

    matched_provider: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="matchedProvider"),
        pydantic.Field(alias="matchedProvider", description="Provider that produced the match, or null when none did."),
    ] = None
    """
    Provider that produced the match, or null when none did.
    """

    aborted: bool = pydantic.Field()
    """
    True when the run was canceled before it settled.
    """

    providers: typing.List[V2EnrichmentProviderOutcome] = pydantic.Field()
    """
    Every configured provider, in cascade order, including those that never ran.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
