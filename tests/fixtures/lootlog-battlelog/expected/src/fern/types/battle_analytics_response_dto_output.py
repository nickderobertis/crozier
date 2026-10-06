

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BattleAnalyticsResponseDtoOutput(UniversalBaseModel):
    total_battles: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalBattles"), pydantic.Field(alias="totalBattles")
    ]
    wins: float
    losses: float
    win_ratio: typing_extensions.Annotated[float, FieldMetadata(alias="winRatio"), pydantic.Field(alias="winRatio")]
    total_ph: typing_extensions.Annotated[float, FieldMetadata(alias="totalPH"), pydantic.Field(alias="totalPH")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
