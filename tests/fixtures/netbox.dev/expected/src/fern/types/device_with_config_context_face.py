

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_with_config_context_face_label import DeviceWithConfigContextFaceLabel
from .device_with_config_context_face_value import DeviceWithConfigContextFaceValue


class DeviceWithConfigContextFace(UniversalBaseModel):
    label: DeviceWithConfigContextFaceLabel
    value: DeviceWithConfigContextFaceValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
