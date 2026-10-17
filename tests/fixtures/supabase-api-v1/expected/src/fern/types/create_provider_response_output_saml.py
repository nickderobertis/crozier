

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_provider_response_output_saml_attribute_mapping import CreateProviderResponseOutputSamlAttributeMapping
from .create_provider_response_output_saml_name_id_format import CreateProviderResponseOutputSamlNameIdFormat


class CreateProviderResponseOutputSaml(UniversalBaseModel):
    entity_id: str
    metadata_url: typing.Optional[str] = None
    metadata_xml: typing.Optional[str] = None
    attribute_mapping: typing.Optional[CreateProviderResponseOutputSamlAttributeMapping] = None
    name_id_format: typing.Optional[CreateProviderResponseOutputSamlNameIdFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
