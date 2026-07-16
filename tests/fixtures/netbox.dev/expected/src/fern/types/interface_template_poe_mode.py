

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .interface_template_poe_mode_label import InterfaceTemplatePoeModeLabel
from .interface_template_poe_mode_value import InterfaceTemplatePoeModeValue


class InterfaceTemplatePoeMode(UniversalBaseModel):
    label: InterfaceTemplatePoeModeLabel
    value: InterfaceTemplatePoeModeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
