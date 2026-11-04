

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .plugin_install_request_source import PluginInstallRequestSource


class PluginInstallRequest(UniversalBaseModel):
    """
    Multipart payload for installing a plugin.
    """

    file: typing.Optional[bytes] = pydantic.Field(default=None)
    """
    Plugin JAR file.
    """

    preset_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="presetName"),
        pydantic.Field(
            alias="presetName", description="Plugin preset name. Halo finds the plugin from plugin presets."
        ),
    ] = None
    """
    Plugin preset name. Halo finds the plugin from plugin presets.
    """

    source: typing.Optional[PluginInstallRequestSource] = pydantic.Field(default=None)
    """
    Install source. Defaults to file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
