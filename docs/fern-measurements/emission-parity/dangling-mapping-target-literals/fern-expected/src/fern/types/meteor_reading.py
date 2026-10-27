

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .meteor_reading_kind import MeteorReadingKind
from .trail import Trail


class MeteorReading(UniversalBaseModel):
    """
    A streak that crossed the sky.
    """

    trail: typing.Optional[Trail] = None
    brightness: typing.Optional[float] = None
    kind: typing.Optional[MeteorReadingKind] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
