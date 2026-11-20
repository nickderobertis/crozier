

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .loom_reading_payload import LoomReadingPayload
from .loom_reading_shuttle import LoomReadingShuttle
from .loom_reading_tension import LoomReadingTension


class LoomReading(UniversalBaseModel):
    payload: LoomReadingPayload
    tension: LoomReadingTension
    shuttle: typing.Optional[LoomReadingShuttle] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
