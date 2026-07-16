

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_historical_stats_destiny_historical_stats_activity import (
    DestinyHistoricalStatsDestinyHistoricalStatsActivity,
)
from .destiny_historical_stats_destiny_historical_stats_value import DestinyHistoricalStatsDestinyHistoricalStatsValue


class DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup(UniversalBaseModel):
    activity_details: typing_extensions.Annotated[
        typing.Optional[DestinyHistoricalStatsDestinyHistoricalStatsActivity],
        FieldMetadata(alias="activityDetails"),
        pydantic.Field(
            alias="activityDetails",
            description="If the period group is for a specific activity, this property will be set.",
        ),
    ] = None
    """
    If the period group is for a specific activity, this property will be set.
    """

    period: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Period for the group. If the stat periodType is day, then this will have a specific day. If the type is monthly, then this value will be the first day of the applicable month. This value is not set when the periodType is 'all time'.
    """

    values: typing.Optional[typing.Dict[str, DestinyHistoricalStatsDestinyHistoricalStatsValue]] = pydantic.Field(
        default=None
    )
    """
    Collection of stats for the period.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
