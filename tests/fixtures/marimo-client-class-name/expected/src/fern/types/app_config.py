

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app_config_auto_download_item import AppConfigAutoDownloadItem
from .app_config_sql_output import AppConfigSqlOutput
from .app_config_width import AppConfigWidth


class AppConfig(UniversalBaseModel):
    """
    Program-specific configuration.

        Configuration for frontends or runtimes that is specific to
        a single marimo program.
    """

    app_title: typing.Optional[str] = None
    auto_download: typing.Optional[typing.List[AppConfigAutoDownloadItem]] = None
    css_file: typing.Optional[str] = None
    html_head_file: typing.Optional[str] = None
    layout_file: typing.Optional[str] = None
    sql_output: typing.Optional[AppConfigSqlOutput] = None
    width: typing.Optional[AppConfigWidth] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
