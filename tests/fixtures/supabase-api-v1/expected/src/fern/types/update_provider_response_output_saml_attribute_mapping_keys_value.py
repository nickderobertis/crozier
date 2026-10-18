

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_provider_response_output_saml_attribute_mapping_keys_value_default import (
    UpdateProviderResponseOutputSamlAttributeMappingKeysValueDefault,
)


class UpdateProviderResponseOutputSamlAttributeMappingKeysValue(UniversalBaseModel):
    name: typing.Optional[str] = None
    names: typing.Optional[typing.List[str]] = None
    array: typing.Optional[bool] = None
    default: typing.Optional[UpdateProviderResponseOutputSamlAttributeMappingKeysValueDefault] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
