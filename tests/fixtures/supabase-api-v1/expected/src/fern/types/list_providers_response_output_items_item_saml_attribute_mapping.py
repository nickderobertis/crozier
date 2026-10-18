

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_providers_response_output_items_item_saml_attribute_mapping_keys_value import (
    ListProvidersResponseOutputItemsItemSamlAttributeMappingKeysValue,
)


class ListProvidersResponseOutputItemsItemSamlAttributeMapping(UniversalBaseModel):
    keys: typing.Dict[str, ListProvidersResponseOutputItemsItemSamlAttributeMappingKeysValue]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
