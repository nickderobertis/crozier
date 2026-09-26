

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_capabilities_interleaved_field_field import ModelCapabilitiesInterleavedFieldField


class ModelCapabilitiesInterleavedField(UniversalBaseModel):
    field: ModelCapabilitiesInterleavedFieldField

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
