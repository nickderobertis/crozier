

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_config_models_value_interleaved_field_field import ProviderConfigModelsValueInterleavedFieldField


class ProviderConfigModelsValueInterleavedField(UniversalBaseModel):
    field: ProviderConfigModelsValueInterleavedFieldField

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
