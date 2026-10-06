

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .battle_raw_response_dto_output_raw_data import BattleRawResponseDtoOutputRawData


class BattleRawResponseDtoOutput(UniversalBaseModel):
    battle_id: typing_extensions.Annotated[str, FieldMetadata(alias="battleId"), pydantic.Field(alias="battleId")]
    timestamp: dt.datetime
    raw_data: typing_extensions.Annotated[
        BattleRawResponseDtoOutputRawData, FieldMetadata(alias="rawData"), pydantic.Field(alias="rawData")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
