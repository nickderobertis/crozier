

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .review_platform_sla import ReviewPlatformSla
from .review_unanswered_buckets import ReviewUnansweredBuckets


class ReviewSlaResponse(UniversalBaseModel):
    """
    Aggregate-only response-SLA metrics. No author, review text, or reply text is carried; platform identifiers are the only non-numeric values.
    """

    total: int = pydantic.Field()
    """
    Total reviews for the business.
    """

    unanswered: int = pydantic.Field()
    """
    Reviews whose reply_status is not "replied".
    """

    answered: int = pydantic.Field()
    """
    Reviews whose reply_status is "replied".
    """

    buckets: ReviewUnansweredBuckets
    target_hours: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="targetHours"),
        pydantic.Field(
            alias="targetHours", description="Answered-within-target window in hours the rate was computed against."
        ),
    ]
    """
    Answered-within-target window in hours the rate was computed against.
    """

    median_response_hours: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="medianResponseHours"),
        pydantic.Field(
            alias="medianResponseHours",
            description="Median response latency in hours (created_at -> replied_at) over measured responses only.",
        ),
    ]
    """
    Median response latency in hours (created_at -> replied_at) over measured responses only.
    """

    average_response_hours: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="averageResponseHours"),
        pydantic.Field(
            alias="averageResponseHours",
            description="Average response latency in hours (created_at -> replied_at) over measured responses only.",
        ),
    ]
    """
    Average response latency in hours (created_at -> replied_at) over measured responses only.
    """

    measured_responses: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="measuredResponses"),
        pydantic.Field(
            alias="measuredResponses",
            description="Replied reviews carrying a replied_at (the denominator behind the median / average / within-target rate).",
        ),
    ]
    """
    Replied reviews carrying a replied_at (the denominator behind the median / average / within-target rate).
    """

    percent_answered_within_target: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="percentAnsweredWithinTarget"),
        pydantic.Field(
            alias="percentAnsweredWithinTarget",
            description="Share of measured responses answered within targetHours, in [0,1].",
        ),
    ]
    """
    Share of measured responses answered within targetHours, in [0,1].
    """

    oldest_unanswered_hours: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="oldestUnansweredHours"),
        pydantic.Field(
            alias="oldestUnansweredHours",
            description="Age in hours of the oldest unanswered review, or null when every review is answered.",
        ),
    ] = None
    """
    Age in hours of the oldest unanswered review, or null when every review is answered.
    """

    platforms: typing.List[ReviewPlatformSla] = pydantic.Field()
    """
    Per-platform medians over the same full measured response set. Platforms without a valid replied_at sample are omitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
