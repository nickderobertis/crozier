

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .led import Led


class RobotStateResponseLeds(UniversalBaseModel):
    system_led: typing_extensions.Annotated[Led, FieldMetadata(alias="systemLed"), pydantic.Field(alias="systemLed")]
    alert_led: typing_extensions.Annotated[Led, FieldMetadata(alias="alertLed"), pydantic.Field(alias="alertLed")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
