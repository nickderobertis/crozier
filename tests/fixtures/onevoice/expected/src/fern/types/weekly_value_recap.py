

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WeeklyValueRecap(UniversalBaseModel):
    """
    Counts of completed operations for one closed Monday-to-Monday UTC week.
    """

    id: str
    week_start: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="weekStart"), pydantic.Field(alias="weekStart")
    ]
    week_end: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="weekEnd"), pydantic.Field(alias="weekEnd")]
    published_posts: typing_extensions.Annotated[
        int, FieldMetadata(alias="publishedPosts"), pydantic.Field(alias="publishedPosts")
    ]
    dispatched_review_replies: typing_extensions.Annotated[
        int, FieldMetadata(alias="dispatchedReviewReplies"), pydantic.Field(alias="dispatchedReviewReplies")
    ]
    completed_syncs: typing_extensions.Annotated[
        int, FieldMetadata(alias="completedSyncs"), pydantic.Field(alias="completedSyncs")
    ]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
