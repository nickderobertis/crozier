

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .battle_raw_response_dto_output_raw_data_events_item_actions_item import (
    BattleRawResponseDtoOutputRawDataEventsItemActionsItem,
)


class BattleRawResponseDtoOutputRawDataEventsItem(UniversalBaseModel):
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
    actions: typing.List[BattleRawResponseDtoOutputRawDataEventsItemActionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
