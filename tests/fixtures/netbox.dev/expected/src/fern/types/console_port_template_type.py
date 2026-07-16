

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .console_port_template_type_label import ConsolePortTemplateTypeLabel
from .console_port_template_type_value import ConsolePortTemplateTypeValue


class ConsolePortTemplateType(UniversalBaseModel):
    label: ConsolePortTemplateTypeLabel
    value: ConsolePortTemplateTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
