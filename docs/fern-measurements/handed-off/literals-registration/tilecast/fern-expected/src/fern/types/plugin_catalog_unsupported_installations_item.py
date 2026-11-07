

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PluginCatalogUnsupportedInstallationsItem(UniversalBaseModel):
    plugin_id: typing_extensions.Annotated[str, FieldMetadata(alias="pluginId"), pydantic.Field(alias="pluginId")]
    installed_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="installedAt"), pydantic.Field(alias="installedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
