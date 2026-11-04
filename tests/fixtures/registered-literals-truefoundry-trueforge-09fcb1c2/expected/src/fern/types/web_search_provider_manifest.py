

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .parallel_web_search_provider_auth import ParallelWebSearchProviderAuth
from .web_search_provider_manifest_type import WebSearchProviderManifestType


class WebSearchProviderManifest(UniversalBaseModel):
    auth: ParallelWebSearchProviderAuth
    type: WebSearchProviderManifestType = pydantic.Field()
    """
    Parallel web-search provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
