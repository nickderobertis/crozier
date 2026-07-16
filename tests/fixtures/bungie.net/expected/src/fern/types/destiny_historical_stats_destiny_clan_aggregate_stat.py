

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_historical_stats_destiny_historical_stats_value import DestinyHistoricalStatsDestinyHistoricalStatsValue


class DestinyHistoricalStatsDestinyClanAggregateStat(UniversalBaseModel):
    mode: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the mode of stats (allPvp, allPvE, etc)
    """

    stat_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="statId"),
        pydantic.Field(alias="statId", description="The id of the stat"),
    ] = None
    """
    The id of the stat
    """

    value: typing.Optional[DestinyHistoricalStatsDestinyHistoricalStatsValue] = pydantic.Field(default=None)
    """
    Value of the stat for this player
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
