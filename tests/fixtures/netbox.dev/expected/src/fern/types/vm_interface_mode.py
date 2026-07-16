

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vm_interface_mode_label import VmInterfaceModeLabel
from .vm_interface_mode_value import VmInterfaceModeValue


class VmInterfaceMode(UniversalBaseModel):
    label: VmInterfaceModeLabel
    value: VmInterfaceModeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
