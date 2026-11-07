

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .available_model_provider import AvailableModelProvider
from .model_properties import ModelProperties


class AvailableModel(UniversalBaseModel):
    model_id: str = pydantic.Field()
    """
    Upstream, provider-specific identifier sent to the provider API.
    """

    name: str = pydantic.Field()
    """
    Fully qualified name `provider_name/model_name`, e.g. "openai/gpt-5-6-sol". Unique within a tenant.
    """

    properties: ModelProperties
    provider: AvailableModelProvider

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
