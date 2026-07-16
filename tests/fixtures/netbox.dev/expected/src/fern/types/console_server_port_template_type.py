

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .console_server_port_template_type_label import ConsoleServerPortTemplateTypeLabel
from .console_server_port_template_type_value import ConsoleServerPortTemplateTypeValue


class ConsoleServerPortTemplateType(UniversalBaseModel):
    label: ConsoleServerPortTemplateTypeLabel
    value: ConsoleServerPortTemplateTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
