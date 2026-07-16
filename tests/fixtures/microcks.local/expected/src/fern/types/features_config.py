

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .features_config_async_api import FeaturesConfigAsyncApi
from .features_config_microcks_hub import FeaturesConfigMicrocksHub
from .features_config_repository_filter import FeaturesConfigRepositoryFilter
from .features_config_repository_tenancy import FeaturesConfigRepositoryTenancy


class FeaturesConfig(UniversalBaseModel):
    """
    Representation of optional features configuration used by Microcks server
    """

    async_api: typing_extensions.Annotated[
        typing.Optional[FeaturesConfigAsyncApi], FieldMetadata(alias="async-api")
    ] = pydantic.Field(default=None)
    """
    Asynchronous feature properties
    """

    microcks_hub: typing_extensions.Annotated[
        typing.Optional[FeaturesConfigMicrocksHub], FieldMetadata(alias="microcks-hub")
    ] = pydantic.Field(default=None)
    """
    Microcks Hub feature properties
    """

    repository_filter: typing_extensions.Annotated[
        typing.Optional[FeaturesConfigRepositoryFilter], FieldMetadata(alias="repository-filter")
    ] = pydantic.Field(default=None)
    """
    Repository filtering feature properties
    """

    repository_tenancy: typing_extensions.Annotated[
        typing.Optional[FeaturesConfigRepositoryTenancy], FieldMetadata(alias="repository-tenancy")
    ] = pydantic.Field(default=None)
    """
    Repository tenancy feature properties
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
