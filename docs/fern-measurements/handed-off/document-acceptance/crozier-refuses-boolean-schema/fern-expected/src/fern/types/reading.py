

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dew_point import DewPoint
from .humidity import Humidity
from .label import Label
from .unit import Unit


class Reading(UniversalBaseModel):
    sensor: str
    humidity: typing.Optional[Humidity] = None
    dew_point: typing_extensions.Annotated[
        typing.Optional[DewPoint], FieldMetadata(alias="dewPoint"), pydantic.Field(alias="dewPoint")
    ] = None
    label: typing.Optional[Label] = None
    unit: typing.Optional[Unit] = None
    tags: typing.Optional[typing.List[typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
