

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .plugin_in_use_error_error_details_resources_item import PluginInUseErrorErrorDetailsResourcesItem


class PluginInUseErrorErrorDetails(UniversalBaseModel):
    plugin_id: typing_extensions.Annotated[str, FieldMetadata(alias="pluginId"), pydantic.Field(alias="pluginId")]
    resources: typing.List[PluginInUseErrorErrorDetailsResourcesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
