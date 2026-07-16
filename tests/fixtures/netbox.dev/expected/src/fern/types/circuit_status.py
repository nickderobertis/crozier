

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .circuit_status_label import CircuitStatusLabel
from .circuit_status_value import CircuitStatusValue


class CircuitStatus(UniversalBaseModel):
    label: CircuitStatusLabel
    value: CircuitStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
