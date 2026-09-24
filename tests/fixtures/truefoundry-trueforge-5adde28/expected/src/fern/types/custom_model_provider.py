

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .configured_model import ConfiguredModel
from .model_provider_auth import ModelProviderAuth
from .resource_name import ResourceName


class CustomModelProvider(UniversalBaseModel):
    auth: typing.Optional[ModelProviderAuth] = None
    base_url: str = pydantic.Field()
    """
    Base URL of the provider's API.
    """

    models: typing.List[ConfiguredModel] = pydantic.Field()
    """
    Models exposed by this provider (at least one).
    """

    name: ResourceName

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
