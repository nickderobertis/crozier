

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .service_template_protocol_label import ServiceTemplateProtocolLabel
from .service_template_protocol_value import ServiceTemplateProtocolValue


class ServiceTemplateProtocol(UniversalBaseModel):
    label: ServiceTemplateProtocolLabel
    value: ServiceTemplateProtocolValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
