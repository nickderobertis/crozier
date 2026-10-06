

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PhGrowthDataPointResponseDtoOutput(UniversalBaseModel):
    date: dt.datetime
    ph: float
    cumulative_ph: typing_extensions.Annotated[
        float, FieldMetadata(alias="cumulativePh"), pydantic.Field(alias="cumulativePh")
    ]
    battle_id: typing_extensions.Annotated[str, FieldMetadata(alias="battleId"), pydantic.Field(alias="battleId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
