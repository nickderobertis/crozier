

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SessionReadingsByOwnerValueValue_Lens(UniversalBaseModel):
    reading_type: typing.Literal["lens"] = "lens"
    focal: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionReadingsByOwnerValueValue_Sensor(UniversalBaseModel):
    reading_type: typing.Literal["sensor"] = "sensor"
    gain: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SessionReadingsByOwnerValueValue = typing_extensions.Annotated[
    typing.Union[SessionReadingsByOwnerValueValue_Lens, SessionReadingsByOwnerValueValue_Sensor],
    pydantic.Field(discriminator="reading_type"),
]
