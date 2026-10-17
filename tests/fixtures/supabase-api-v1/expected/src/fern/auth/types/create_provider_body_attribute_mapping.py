

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_provider_body_attribute_mapping_keys_value import CreateProviderBodyAttributeMappingKeysValue


class CreateProviderBodyAttributeMapping(UniversalBaseModel):
    keys: typing.Dict[str, CreateProviderBodyAttributeMappingKeysValue]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
