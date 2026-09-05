

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1alpha1plugin_metadata import V1Alpha1PluginMetadata


class V1Alpha1Plugin(UniversalBaseModel):
    name: str
    metadata: V1Alpha1PluginMetadata
    module: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
