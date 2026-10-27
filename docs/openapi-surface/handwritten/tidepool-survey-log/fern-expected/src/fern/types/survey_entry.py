

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .water_level import WaterLevel


class SurveyEntry_Level(UniversalBaseModel):
    value: WaterLevel
    entry_type: typing_extensions.Annotated[
        typing.Literal["level"], FieldMetadata(alias="entryType"), pydantic.Field(alias="entryType")
    ] = "level"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


class SurveyEntry_Sighting(UniversalBaseModel):
    """
    One thing a volunteer recorded at the pool.
    """

    entry_type: typing_extensions.Annotated[
        typing.Literal["sighting"], FieldMetadata(alias="entryType"), pydantic.Field(alias="entryType")
    ] = "sighting"
    species: str
    count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SurveyEntry = typing_extensions.Annotated[
    typing.Union[SurveyEntry_Level, SurveyEntry_Sighting], pydantic.Field(discriminator="entry_type")
]
