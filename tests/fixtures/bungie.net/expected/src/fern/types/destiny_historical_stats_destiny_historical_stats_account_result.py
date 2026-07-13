

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_historical_stats_destiny_historical_stats_per_character import (
    DestinyHistoricalStatsDestinyHistoricalStatsPerCharacter,
)
from .destiny_historical_stats_destiny_historical_stats_with_merged import (
    DestinyHistoricalStatsDestinyHistoricalStatsWithMerged,
)


class DestinyHistoricalStatsDestinyHistoricalStatsAccountResult(UniversalBaseModel):
    characters: typing.Optional[typing.List[DestinyHistoricalStatsDestinyHistoricalStatsPerCharacter]] = None
    merged_all_characters: typing_extensions.Annotated[
        typing.Optional[DestinyHistoricalStatsDestinyHistoricalStatsWithMerged],
        FieldMetadata(alias="mergedAllCharacters"),
    ] = None
    merged_deleted_characters: typing_extensions.Annotated[
        typing.Optional[DestinyHistoricalStatsDestinyHistoricalStatsWithMerged],
        FieldMetadata(alias="mergedDeletedCharacters"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
