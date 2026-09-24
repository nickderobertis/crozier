

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .limit_switch import LimitSwitch


class LimitSwitchState(UniversalBaseModel):
    limit_switch1: typing_extensions.Annotated[
        LimitSwitch, FieldMetadata(alias="limitSwitch1"), pydantic.Field(alias="limitSwitch1")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
