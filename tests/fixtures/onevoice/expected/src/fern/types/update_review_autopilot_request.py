

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateReviewAutopilotRequest(UniversalBaseModel):
    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Opt-in switch for the review-reply autopilot. When true, a positive
    drafted reply on a direct-API platform (Telegram/VK) is auto-published;
    Yandex.Business, negative, and needs_review replies always stay pending
    for manual approval. Absent is treated as false (disabled).
    """

    min_rating: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="minRating"),
        pydantic.Field(
            alias="minRating",
            description="The minimum star rating that may be auto-published. Bounded to the\npositive range so the floor can only be raised (e.g. 5-star-only) and\ncan never be lowered to auto-publish a negative or neutral review.",
        ),
    ]
    """
    The minimum star rating that may be auto-published. Bounded to the
    positive range so the floor can only be raised (e.g. 5-star-only) and
    can never be lowered to auto-publish a negative or neutral review.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
