

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .battle_timeline_response_dto_output_timeline_item_actions_item import (
    BattleTimelineResponseDtoOutputTimelineItemActionsItem,
)
from .battle_timeline_response_dto_output_timeline_item_cumulative_value import (
    BattleTimelineResponseDtoOutputTimelineItemCumulativeValue,
)
from .battle_timeline_response_dto_output_timeline_item_deltas import BattleTimelineResponseDtoOutputTimelineItemDeltas


class BattleTimelineResponseDtoOutputTimelineItem(UniversalBaseModel):
    turn: float
    attacker_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="attackerId"), pydantic.Field(alias="attackerId")
    ] = None
    defender_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="defenderId"), pydantic.Field(alias="defenderId")
    ] = None
    attacker_hp_percentage: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="attackerHpPercentage"),
        pydantic.Field(alias="attackerHpPercentage"),
    ] = None
    defender_hp_percentage: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="defenderHpPercentage"),
        pydantic.Field(alias="defenderHpPercentage"),
    ] = None
    hp_by_warrior: typing_extensions.Annotated[
        typing.Dict[str, float], FieldMetadata(alias="hpByWarrior"), pydantic.Field(alias="hpByWarrior")
    ]
    team_hp: typing_extensions.Annotated[
        typing.Dict[str, float], FieldMetadata(alias="teamHp"), pydantic.Field(alias="teamHp")
    ]
    team_hp_delta: typing_extensions.Annotated[
        typing.Dict[str, float], FieldMetadata(alias="teamHpDelta"), pydantic.Field(alias="teamHpDelta")
    ]
    deltas: BattleTimelineResponseDtoOutputTimelineItemDeltas
    cumulative: typing.Dict[str, BattleTimelineResponseDtoOutputTimelineItemCumulativeValue]
    actions: typing.List[BattleTimelineResponseDtoOutputTimelineItemActionsItem]
    flags: typing.List[str]
    labels: typing.List[str]
    significance_score: typing_extensions.Annotated[
        float, FieldMetadata(alias="significanceScore"), pydantic.Field(alias="significanceScore")
    ]
    reason: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
