

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vlan_status_label import VlanStatusLabel
from .vlan_status_value import VlanStatusValue


class VlanStatus(UniversalBaseModel):
    label: VlanStatusLabel
    value: VlanStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
