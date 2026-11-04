

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_properties import ModelProperties
from .resource_name import ResourceName


class ConfiguredModel(UniversalBaseModel):
    model_id: str = pydantic.Field()
    """
    Upstream, provider-specific identifier sent to the provider API.
    """

    name: ResourceName
    properties: ModelProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
