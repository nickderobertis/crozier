

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_providers_response_output_items_item_domains_item import ListProvidersResponseOutputItemsItemDomainsItem
from .list_providers_response_output_items_item_saml import ListProvidersResponseOutputItemsItemSaml


class ListProvidersResponseOutputItemsItem(UniversalBaseModel):
    id: str
    saml: typing.Optional[ListProvidersResponseOutputItemsItemSaml] = None
    domains: typing.Optional[typing.List[ListProvidersResponseOutputItemsItemDomainsItem]] = None
    created_at: typing.Optional[str] = None
    updated_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
