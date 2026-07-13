

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_historical_stats_destiny_historical_weapon_stats import DestinyHistoricalStatsDestinyHistoricalWeaponStats


class DestinyHistoricalStatsDestinyHistoricalWeaponStatsData(UniversalBaseModel):
    weapons: typing.Optional[typing.List[DestinyHistoricalStatsDestinyHistoricalWeaponStats]] = pydantic.Field(
        default=None
    )
    """
    List of weapons and their perspective values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
