

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .interface_poe_type_label import InterfacePoeTypeLabel
from .interface_poe_type_value import InterfacePoeTypeValue


class InterfacePoeType(UniversalBaseModel):
    label: InterfacePoeTypeLabel
    value: InterfacePoeTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
