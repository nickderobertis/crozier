

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_provider_response_output_saml_attribute_mapping import GetProviderResponseOutputSamlAttributeMapping
from .get_provider_response_output_saml_name_id_format import GetProviderResponseOutputSamlNameIdFormat


class GetProviderResponseOutputSaml(UniversalBaseModel):
    entity_id: str
    metadata_url: typing.Optional[str] = None
    metadata_xml: typing.Optional[str] = None
    attribute_mapping: typing.Optional[GetProviderResponseOutputSamlAttributeMapping] = None
    name_id_format: typing.Optional[GetProviderResponseOutputSamlNameIdFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
