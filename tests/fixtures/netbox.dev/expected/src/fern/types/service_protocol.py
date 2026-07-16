

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .service_protocol_label import ServiceProtocolLabel
from .service_protocol_value import ServiceProtocolValue


class ServiceProtocol(UniversalBaseModel):
    label: ServiceProtocolLabel
    value: ServiceProtocolValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
