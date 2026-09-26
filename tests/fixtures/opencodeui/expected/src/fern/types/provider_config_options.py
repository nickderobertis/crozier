

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .provider_config_options_timeout import ProviderConfigOptionsTimeout


class ProviderConfigOptions(UniversalBaseModel):
    api_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiKey"), pydantic.Field(alias="apiKey")
    ] = None
    base_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="baseURL"), pydantic.Field(alias="baseURL")
    ] = None
    enterprise_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="enterpriseUrl"),
        pydantic.Field(alias="enterpriseUrl", description="GitHub Enterprise URL for copilot authentication"),
    ] = None
    """
    GitHub Enterprise URL for copilot authentication
    """

    set_cache_key: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="setCacheKey"),
        pydantic.Field(alias="setCacheKey", description="Enable promptCacheKey for this provider (default false)"),
    ] = None
    """
    Enable promptCacheKey for this provider (default false)
    """

    timeout: typing.Optional[ProviderConfigOptionsTimeout] = pydantic.Field(default=None)
    """
    Timeout in milliseconds for requests to this provider. Default is 300000 (5 minutes). Set to false to disable timeout.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
