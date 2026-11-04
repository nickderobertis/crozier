

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resource_name import ResourceName
from .web_search_provider_manifest import WebSearchProviderManifest


class ConfiguredWebSearchProvider(UniversalBaseModel):
    manifest: WebSearchProviderManifest
    name: ResourceName

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
