

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .interface_type_label import InterfaceTypeLabel
from .interface_type_value import InterfaceTypeValue


class InterfaceType(UniversalBaseModel):
    label: InterfaceTypeLabel
    value: InterfaceTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
