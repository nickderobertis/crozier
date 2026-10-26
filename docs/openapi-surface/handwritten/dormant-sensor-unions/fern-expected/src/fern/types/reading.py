

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lull import Lull
from .pitch import Pitch
from .reading_mode import ReadingMode
from .silence import Silence
from .stillness import Stillness
from .tone import Tone


class Reading(UniversalBaseModel):
    label: str
    silence: typing.Optional[Silence] = None
    lull: typing.Optional[Lull] = None
    hush: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    stillness: typing.Optional[Stillness] = None
    void: typing.Optional[typing.Any] = None
    pitch: typing.Optional[Pitch] = None
    tone: typing.Optional[Tone] = None
    mode: typing.Optional[ReadingMode] = pydantic.Field(default=None)
    """
    Whether the sensor is sampling.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
