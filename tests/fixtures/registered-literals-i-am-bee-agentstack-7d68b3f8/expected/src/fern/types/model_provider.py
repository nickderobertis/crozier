

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_system_model_provider_registry_location import FileSystemModelProviderRegistryLocation
from .model_capability import ModelCapability
from .model_provider_state import ModelProviderState
from .model_provider_type import ModelProviderType


class ModelProvider(UniversalBaseModel):
    id: typing.Optional[str] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable name for the model provider
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional description of the provider
    """

    type: ModelProviderType = pydantic.Field()
    """
    Type of model provider
    """

    base_url: str = pydantic.Field()
    """
    Base URL for the API (unique)
    """

    created_at: typing.Optional[dt.datetime] = None
    registry: typing.Optional[FileSystemModelProviderRegistryLocation] = None
    state: typing.Optional[ModelProviderState] = None
    capabilities: typing.Optional[typing.List[ModelCapability]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
