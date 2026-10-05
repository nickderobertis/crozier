

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .battles_list_response_dto_output_battles_item_statistics_best_efficiency import (
    BattlesListResponseDtoOutputBattlesItemStatisticsBestEfficiency,
)
from .battles_list_response_dto_output_battles_item_statistics_critical_master import (
    BattlesListResponseDtoOutputBattlesItemStatisticsCriticalMaster,
)
from .battles_list_response_dto_output_battles_item_statistics_damage_per_turn import (
    BattlesListResponseDtoOutputBattlesItemStatisticsDamagePerTurn,
)
from .battles_list_response_dto_output_battles_item_statistics_evasion_expert import (
    BattlesListResponseDtoOutputBattlesItemStatisticsEvasionExpert,
)
from .battles_list_response_dto_output_battles_item_statistics_legendary_warrior import (
    BattlesListResponseDtoOutputBattlesItemStatisticsLegendaryWarrior,
)
from .battles_list_response_dto_output_battles_item_statistics_most_active import (
    BattlesListResponseDtoOutputBattlesItemStatisticsMostActive,
)
from .battles_list_response_dto_output_battles_item_statistics_shield_wall import (
    BattlesListResponseDtoOutputBattlesItemStatisticsShieldWall,
)
from .battles_list_response_dto_output_battles_item_statistics_top_damage_dealer import (
    BattlesListResponseDtoOutputBattlesItemStatisticsTopDamageDealer,
)
from .battles_list_response_dto_output_battles_item_statistics_top_tank import (
    BattlesListResponseDtoOutputBattlesItemStatisticsTopTank,
)
from .battles_list_response_dto_output_battles_item_statistics_untouchable import (
    BattlesListResponseDtoOutputBattlesItemStatisticsUntouchable,
)


class BattlesListResponseDtoOutputBattlesItemStatistics(UniversalBaseModel):
    top_damage_dealer: typing_extensions.Annotated[
        typing.Optional[BattlesListResponseDtoOutputBattlesItemStatisticsTopDamageDealer],
        FieldMetadata(alias="topDamageDealer"),
        pydantic.Field(alias="topDamageDealer"),
    ] = None
    top_tank: typing_extensions.Annotated[
        typing.Optional[BattlesListResponseDtoOutputBattlesItemStatisticsTopTank],
        FieldMetadata(alias="topTank"),
        pydantic.Field(alias="topTank"),
    ] = None
    best_efficiency: typing_extensions.Annotated[
        typing.Optional[BattlesListResponseDtoOutputBattlesItemStatisticsBestEfficiency],
        FieldMetadata(alias="bestEfficiency"),
        pydantic.Field(alias="bestEfficiency"),
    ] = None
    critical_master: typing_extensions.Annotated[
        typing.Optional[BattlesListResponseDtoOutputBattlesItemStatisticsCriticalMaster],
        FieldMetadata(alias="criticalMaster"),
        pydantic.Field(alias="criticalMaster"),
    ] = None
    evasion_expert: typing_extensions.Annotated[
        typing.Optional[BattlesListResponseDtoOutputBattlesItemStatisticsEvasionExpert],
        FieldMetadata(alias="evasionExpert"),
        pydantic.Field(alias="evasionExpert"),
    ] = None
    shield_wall: typing_extensions.Annotated[
        typing.Optional[BattlesListResponseDtoOutputBattlesItemStatisticsShieldWall],
        FieldMetadata(alias="shieldWall"),
        pydantic.Field(alias="shieldWall"),
    ] = None
    damage_per_turn: typing_extensions.Annotated[
        typing.Optional[BattlesListResponseDtoOutputBattlesItemStatisticsDamagePerTurn],
        FieldMetadata(alias="damagePerTurn"),
        pydantic.Field(alias="damagePerTurn"),
    ] = None
    most_active: typing_extensions.Annotated[
        typing.Optional[BattlesListResponseDtoOutputBattlesItemStatisticsMostActive],
        FieldMetadata(alias="mostActive"),
        pydantic.Field(alias="mostActive"),
    ] = None
    legendary_warrior: typing_extensions.Annotated[
        typing.Optional[BattlesListResponseDtoOutputBattlesItemStatisticsLegendaryWarrior],
        FieldMetadata(alias="legendaryWarrior"),
        pydantic.Field(alias="legendaryWarrior"),
    ] = None
    untouchable: typing.Optional[BattlesListResponseDtoOutputBattlesItemStatisticsUntouchable] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
