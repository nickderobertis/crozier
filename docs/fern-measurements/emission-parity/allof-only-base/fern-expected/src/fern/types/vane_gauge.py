

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .calibrated import Calibrated
from .gauge import Gauge


class VaneGauge(Gauge, Calibrated):
    heading: typing.Optional[float] = None
    degrees: typing.Optional[float] = None
    compass_point: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="compassPoint"), pydantic.Field(alias="compassPoint")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
