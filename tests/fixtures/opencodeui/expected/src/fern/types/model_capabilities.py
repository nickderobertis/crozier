

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_capabilities_input import ModelCapabilitiesInput
from .model_capabilities_interleaved import ModelCapabilitiesInterleaved
from .model_capabilities_output import ModelCapabilitiesOutput


class ModelCapabilities(UniversalBaseModel):
    temperature: bool
    reasoning: bool
    attachment: bool
    toolcall: bool
    input: ModelCapabilitiesInput
    output: ModelCapabilitiesOutput
    interleaved: ModelCapabilitiesInterleaved

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
