

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RatingGrowthDataPointResponseDtoOutput(UniversalBaseModel):
    date: dt.datetime
    rating_delta: typing_extensions.Annotated[
        float, FieldMetadata(alias="ratingDelta"), pydantic.Field(alias="ratingDelta")
    ]
    rating: float
    battle_id: typing_extensions.Annotated[str, FieldMetadata(alias="battleId"), pydantic.Field(alias="battleId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
