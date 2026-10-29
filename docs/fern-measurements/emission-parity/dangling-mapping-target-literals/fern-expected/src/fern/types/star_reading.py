

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .star_reading_kind import StarReadingKind


class StarReading(UniversalBaseModel):
    kind: typing.Optional[StarReadingKind] = None
    magnitude: typing.Optional[float] = None
    constellation: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
