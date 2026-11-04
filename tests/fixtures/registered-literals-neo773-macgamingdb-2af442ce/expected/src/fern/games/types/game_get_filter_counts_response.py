

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GameGetFilterCountsResponse(UniversalBaseModel):
    all_: typing_extensions.Annotated[float, FieldMetadata(alias="ALL"), pydantic.Field(alias="ALL")]
    excellent: typing_extensions.Annotated[float, FieldMetadata(alias="EXCELLENT"), pydantic.Field(alias="EXCELLENT")]
    very_good: typing_extensions.Annotated[float, FieldMetadata(alias="VERY_GOOD"), pydantic.Field(alias="VERY_GOOD")]
    good: typing_extensions.Annotated[float, FieldMetadata(alias="GOOD"), pydantic.Field(alias="GOOD")]
    playable: typing_extensions.Annotated[float, FieldMetadata(alias="PLAYABLE"), pydantic.Field(alias="PLAYABLE")]
    barely_playable: typing_extensions.Annotated[
        float, FieldMetadata(alias="BARELY_PLAYABLE"), pydantic.Field(alias="BARELY_PLAYABLE")
    ]
    unplayable: typing_extensions.Annotated[
        float, FieldMetadata(alias="UNPLAYABLE"), pydantic.Field(alias="UNPLAYABLE")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
