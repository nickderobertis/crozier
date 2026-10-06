

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BattleResponseDtoOutputStatisticsTopTank(UniversalBaseModel):
    warrior_id: typing_extensions.Annotated[str, FieldMetadata(alias="warriorId"), pydantic.Field(alias="warriorId")]
    name: str
    value: float
    formatted_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="formattedValue"), pydantic.Field(alias="formattedValue")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
