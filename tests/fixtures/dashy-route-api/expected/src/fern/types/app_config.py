

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_config_icon_size import AppConfigIconSize
from .app_config_layout import AppConfigLayout
from .app_config_starting_view import AppConfigStartingView


class AppConfig(UniversalBaseModel):
    """
    Global app settings (theme, layout, status checks, auth, etc.). Many fields are
    supported. See the [configuring docs](https://github.com/Lissy93/dashy/blob/master/docs/configuring.md).
    """

    theme: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default theme name
    """

    layout: typing.Optional[AppConfigLayout] = pydantic.Field(default=None)
    """
    Section layout
    """

    icon_size: typing_extensions.Annotated[
        typing.Optional[AppConfigIconSize],
        FieldMetadata(alias="iconSize"),
        pydantic.Field(alias="iconSize", description="Item icon size"),
    ] = None
    """
    Item icon size
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    UI language code
    """

    starting_view: typing_extensions.Annotated[
        typing.Optional[AppConfigStartingView],
        FieldMetadata(alias="startingView"),
        pydantic.Field(alias="startingView", description="Initial view"),
    ] = None
    """
    Initial view
    """

    status_check: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="statusCheck"),
        pydantic.Field(alias="statusCheck", description="Enable status checks globally"),
    ] = None
    """
    Enable status checks globally
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
