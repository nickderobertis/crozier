

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .battle_timeline_response_dto_output_timeline_item import BattleTimelineResponseDtoOutputTimelineItem
from .battle_timeline_response_dto_output_warriors_item import BattleTimelineResponseDtoOutputWarriorsItem


class BattleTimelineResponseDtoOutput(UniversalBaseModel):
    battle_id: typing_extensions.Annotated[str, FieldMetadata(alias="battleId"), pydantic.Field(alias="battleId")]
    generated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="generatedAt"), pydantic.Field(alias="generatedAt")
    ]
    timeline: typing.List[BattleTimelineResponseDtoOutputTimelineItem]
    warriors: typing.List[BattleTimelineResponseDtoOutputWarriorsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
