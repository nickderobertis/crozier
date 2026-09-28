

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PresenceSubScores(UniversalBaseModel):
    """
    The four normalized 0-100 presence-health dimensions. rating, sla, and coverage are null in the empty state (no reviews); sync is null when the business has no connected-channel sync signal (the sync dimension is dropped and the other weights renormalize).
    """

    rating_score: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ratingScore"),
        pydantic.Field(
            alias="ratingScore", description="Average star rating normalized to 0-100. Null when no rated reviews."
        ),
    ] = None
    """
    Average star rating normalized to 0-100. Null when no rated reviews.
    """

    sla_score: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="slaScore"),
        pydantic.Field(
            alias="slaScore",
            description="Percent answered within target normalized to 0-100. Null when no measurable responses.",
        ),
    ] = None
    """
    Percent answered within target normalized to 0-100. Null when no measurable responses.
    """

    coverage_score: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="coverageScore"),
        pydantic.Field(
            alias="coverageScore", description="Answered share (replied / total) as 0-100. Null when no reviews."
        ),
    ] = None
    """
    Answered share (replied / total) as 0-100. Null when no reviews.
    """

    sync_score: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="syncScore"),
        pydantic.Field(
            alias="syncScore", description="Connected-channel sync health as 0-100. Null when no sync signal exists."
        ),
    ] = None
    """
    Connected-channel sync health as 0-100. Null when no sync signal exists.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
