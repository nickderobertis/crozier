

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .module_status_label import ModuleStatusLabel
from .module_status_value import ModuleStatusValue


class ModuleStatus(UniversalBaseModel):
    label: ModuleStatusLabel
    value: ModuleStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
