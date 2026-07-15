

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PluginCollectionItem(UniversalBaseModel):
    """
    A plugin Item.

    *New in version 2.1.0*
    """

    appbuilder_menu_items: typing.Optional[
        typing.List[typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]]
    ] = pydantic.Field(default=None)
    """
    The Flask Appbuilder menu items
    """

    appbuilder_views: typing.Optional[typing.List[typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]]] = (
        pydantic.Field(default=None)
    )
    """
    The appuilder views
    """

    executors: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(default=None)
    """
    The plugin executors
    """

    flask_blueprints: typing.Optional[typing.List[typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]]] = (
        pydantic.Field(default=None)
    )
    """
    The flask blueprints
    """

    global_operator_extra_links: typing.Optional[
        typing.List[typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]]
    ] = pydantic.Field(default=None)
    """
    The global operator extra links
    """

    hooks: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(default=None)
    """
    The plugin hooks
    """

    macros: typing.Optional[typing.List[typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]]] = (
        pydantic.Field(default=None)
    )
    """
    The plugin macros
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the plugin
    """

    operator_extra_links: typing.Optional[
        typing.List[typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]]
    ] = pydantic.Field(default=None)
    """
    Operator extra links
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    The plugin source
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
