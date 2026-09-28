

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .review_delegation_week import ReviewDelegationWeek


class ReviewDelegationMetrics(UniversalBaseModel):
    """
    Aggregate feedback on saved draft replies with replied_at in the recent weekly interval. Unknown counts timestamped replies without an edit signal. Legacy rows missing replied_at cannot be assigned to a week and are excluded from all totals.
    """

    from_: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    to: dt.datetime
    replied: int
    accepted_unedited: typing_extensions.Annotated[
        int, FieldMetadata(alias="acceptedUnedited"), pydantic.Field(alias="acceptedUnedited")
    ]
    edited: int
    unknown: int
    measurable: int = pydantic.Field()
    """
    acceptedUnedited plus edited; the denominator for known-feedback shares.
    """

    weeks: typing.List[ReviewDelegationWeek]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
