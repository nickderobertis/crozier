

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_face_label import DeviceFaceLabel
from .device_face_value import DeviceFaceValue


class DeviceFace(UniversalBaseModel):
    label: DeviceFaceLabel
    value: DeviceFaceValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
