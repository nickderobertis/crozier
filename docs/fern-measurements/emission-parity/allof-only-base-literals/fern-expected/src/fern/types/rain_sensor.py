

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .gauge import Gauge


class RainSensor(Gauge):
    millimetres: typing.Optional[float] = None
    bucket: typing.Optional[str] = None
    funnel_width: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="funnelWidth"), pydantic.Field(alias="funnelWidth")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
