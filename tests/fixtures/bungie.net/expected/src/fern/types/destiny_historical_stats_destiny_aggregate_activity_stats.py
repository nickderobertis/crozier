

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_historical_stats_destiny_historical_stats_value import DestinyHistoricalStatsDestinyHistoricalStatsValue


class DestinyHistoricalStatsDestinyAggregateActivityStats(UniversalBaseModel):
    activity_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityHash")] = (
        pydantic.Field(default=None)
    )
    """
    Hash ID that can be looked up in the DestinyActivityTable.
    """

    values: typing.Optional[typing.Dict[str, DestinyHistoricalStatsDestinyHistoricalStatsValue]] = pydantic.Field(
        default=None
    )
    """
    Collection of stats for the player in this activity.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
