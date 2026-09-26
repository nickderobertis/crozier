

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .presence_recommendation import PresenceRecommendation
from .presence_sub_scores import PresenceSubScores
from .presence_weights import PresenceWeights


class PresenceHealthResponse(UniversalBaseModel):
    """
    Read-only composite presence-health score. Aggregate-only: no author, review text, or reply text is carried — numbers only. composite and trendDelta are null when there is not yet enough data.
    """

    composite: typing.Optional[int] = pydantic.Field(default=None)
    """
    The weighted 0-100 composite. Null in the empty state (no reviews).
    """

    trend_delta: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="trendDelta"),
        pydantic.Field(
            alias="trendDelta",
            description="composite minus the most-recent prior-week snapshot's composite. Null when no prior-week snapshot exists.",
        ),
    ] = None
    """
    composite minus the most-recent prior-week snapshot's composite. Null when no prior-week snapshot exists.
    """

    sub_scores: typing_extensions.Annotated[
        PresenceSubScores, FieldMetadata(alias="subScores"), pydantic.Field(alias="subScores")
    ]
    weights: PresenceWeights
    top_recommendation: typing_extensions.Annotated[
        typing.Optional[PresenceRecommendation],
        FieldMetadata(alias="topRecommendation"),
        pydantic.Field(alias="topRecommendation", description="The single next-action nudge. Null in the empty state."),
    ] = None
    """
    The single next-action nudge. Null in the empty state.
    """

    computed_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="computedAt"),
        pydantic.Field(alias="computedAt", description="When the score was computed."),
    ]
    """
    When the score was computed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
