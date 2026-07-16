

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .interface_template_type_label import InterfaceTemplateTypeLabel
from .interface_template_type_value import InterfaceTemplateTypeValue


class InterfaceTemplateType(UniversalBaseModel):
    label: InterfaceTemplateTypeLabel
    value: InterfaceTemplateTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
