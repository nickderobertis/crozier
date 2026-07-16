

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .virtual_machine_with_config_context_status_label import VirtualMachineWithConfigContextStatusLabel
from .virtual_machine_with_config_context_status_value import VirtualMachineWithConfigContextStatusValue


class VirtualMachineWithConfigContextStatus(UniversalBaseModel):
    label: VirtualMachineWithConfigContextStatusLabel
    value: VirtualMachineWithConfigContextStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
