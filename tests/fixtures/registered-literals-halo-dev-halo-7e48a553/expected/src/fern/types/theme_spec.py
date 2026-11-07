

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .author import Author
from .custom_templates import CustomTemplates
from .license import License


class ThemeSpec(UniversalBaseModel):
    """
    Desired theme metadata and configuration references.
    """

    author: Author
    config_map_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="configMapName"),
        pydantic.Field(
            alias="configMapName", description="ConfigMap metadata.name storing the theme configuration values."
        ),
    ] = None
    """
    ConfigMap metadata.name storing the theme configuration values.
    """

    custom_templates: typing_extensions.Annotated[
        typing.Optional[CustomTemplates],
        FieldMetadata(alias="customTemplates"),
        pydantic.Field(alias="customTemplates"),
    ] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable theme description.
    """

    display_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name shown for the theme."),
    ]
    """
    Display name shown for the theme.
    """

    homepage: typing.Optional[str] = pydantic.Field(default=None)
    """
    Theme homepage URL.
    """

    issues: typing.Optional[str] = pydantic.Field(default=None)
    """
    Issue tracker URL.
    """

    license: typing.Optional[typing.List[License]] = pydantic.Field(default=None)
    """
    Licenses declared by the theme.
    """

    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Logo URL or attachment URI for the theme.
    """

    repo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Source repository URL.
    """

    requires: typing.Optional[str] = pydantic.Field(default=None)
    """
    Required Halo version range. The wildcard value means any Halo version.
    """

    setting_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="settingName"),
        pydantic.Field(
            alias="settingName", description="Setting metadata.name used to render the theme configuration form."
        ),
    ] = None
    """
    Setting metadata.name used to render the theme configuration form.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Theme version. The wildcard value means any version.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
