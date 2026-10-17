

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_provider_response_output_saml_attribute_mapping_keys_value import (
    CreateProviderResponseOutputSamlAttributeMappingKeysValue,
)


class CreateProviderResponseOutputSamlAttributeMapping(UniversalBaseModel):
    keys: typing.Dict[str, CreateProviderResponseOutputSamlAttributeMappingKeysValue]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
