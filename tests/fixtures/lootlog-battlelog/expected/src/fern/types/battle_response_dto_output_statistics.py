

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .battle_response_dto_output_statistics_best_efficiency import BattleResponseDtoOutputStatisticsBestEfficiency
from .battle_response_dto_output_statistics_critical_master import BattleResponseDtoOutputStatisticsCriticalMaster
from .battle_response_dto_output_statistics_damage_per_turn import BattleResponseDtoOutputStatisticsDamagePerTurn
from .battle_response_dto_output_statistics_evasion_expert import BattleResponseDtoOutputStatisticsEvasionExpert
from .battle_response_dto_output_statistics_legendary_warrior import BattleResponseDtoOutputStatisticsLegendaryWarrior
from .battle_response_dto_output_statistics_most_active import BattleResponseDtoOutputStatisticsMostActive
from .battle_response_dto_output_statistics_shield_wall import BattleResponseDtoOutputStatisticsShieldWall
from .battle_response_dto_output_statistics_top_damage_dealer import BattleResponseDtoOutputStatisticsTopDamageDealer
from .battle_response_dto_output_statistics_top_tank import BattleResponseDtoOutputStatisticsTopTank
from .battle_response_dto_output_statistics_untouchable import BattleResponseDtoOutputStatisticsUntouchable


class BattleResponseDtoOutputStatistics(UniversalBaseModel):
    top_damage_dealer: typing_extensions.Annotated[
        typing.Optional[BattleResponseDtoOutputStatisticsTopDamageDealer],
        FieldMetadata(alias="topDamageDealer"),
        pydantic.Field(alias="topDamageDealer"),
    ] = None
    top_tank: typing_extensions.Annotated[
        typing.Optional[BattleResponseDtoOutputStatisticsTopTank],
        FieldMetadata(alias="topTank"),
        pydantic.Field(alias="topTank"),
    ] = None
    best_efficiency: typing_extensions.Annotated[
        typing.Optional[BattleResponseDtoOutputStatisticsBestEfficiency],
        FieldMetadata(alias="bestEfficiency"),
        pydantic.Field(alias="bestEfficiency"),
    ] = None
    critical_master: typing_extensions.Annotated[
        typing.Optional[BattleResponseDtoOutputStatisticsCriticalMaster],
        FieldMetadata(alias="criticalMaster"),
        pydantic.Field(alias="criticalMaster"),
    ] = None
    evasion_expert: typing_extensions.Annotated[
        typing.Optional[BattleResponseDtoOutputStatisticsEvasionExpert],
        FieldMetadata(alias="evasionExpert"),
        pydantic.Field(alias="evasionExpert"),
    ] = None
    shield_wall: typing_extensions.Annotated[
        typing.Optional[BattleResponseDtoOutputStatisticsShieldWall],
        FieldMetadata(alias="shieldWall"),
        pydantic.Field(alias="shieldWall"),
    ] = None
    damage_per_turn: typing_extensions.Annotated[
        typing.Optional[BattleResponseDtoOutputStatisticsDamagePerTurn],
        FieldMetadata(alias="damagePerTurn"),
        pydantic.Field(alias="damagePerTurn"),
    ] = None
    most_active: typing_extensions.Annotated[
        typing.Optional[BattleResponseDtoOutputStatisticsMostActive],
        FieldMetadata(alias="mostActive"),
        pydantic.Field(alias="mostActive"),
    ] = None
    legendary_warrior: typing_extensions.Annotated[
        typing.Optional[BattleResponseDtoOutputStatisticsLegendaryWarrior],
        FieldMetadata(alias="legendaryWarrior"),
        pydantic.Field(alias="legendaryWarrior"),
    ] = None
    untouchable: typing.Optional[BattleResponseDtoOutputStatisticsUntouchable] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
