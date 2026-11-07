

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .license import License
from .plugin_author import PluginAuthor


class PluginSpec(UniversalBaseModel):
    """
    Desired plugin metadata and configuration references.
    """

    author: typing.Optional[PluginAuthor] = None
    config_map_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="configMapName"),
        pydantic.Field(
            alias="configMapName", description="ConfigMap metadata.name storing plugin configuration values."
        ),
    ] = None
    """
    ConfigMap metadata.name storing plugin configuration values.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable plugin description.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name shown for the plugin."),
    ] = None
    """
    Display name shown for the plugin.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the plugin should be enabled.
    """

    homepage: typing.Optional[str] = pydantic.Field(default=None)
    """
    Plugin homepage URL.
    """

    issues: typing.Optional[str] = pydantic.Field(default=None)
    """
    Issue tracker URL.
    """

    license: typing.Optional[typing.List[License]] = pydantic.Field(default=None)
    """
    Licenses declared by the plugin.
    """

    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Logo URL or attachment URI for the plugin.
    """

    plugin_dependencies: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="pluginDependencies"),
        pydantic.Field(
            alias="pluginDependencies",
            description="Required plugin dependencies keyed by plugin name with version constraints as values.",
        ),
    ] = None
    """
    Required plugin dependencies keyed by plugin name with version constraints as values.
    """

    repo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Source repository URL.
    """

    requires: typing.Optional[str] = pydantic.Field(default=None)
    """
    SemVer format.
    """

    setting_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="settingName"),
        pydantic.Field(
            alias="settingName", description="Setting metadata.name used to render the plugin configuration form."
        ),
    ] = None
    """
    Setting metadata.name used to render the plugin configuration form.
    """

    version: str = pydantic.Field()
    """
    plugin version.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
