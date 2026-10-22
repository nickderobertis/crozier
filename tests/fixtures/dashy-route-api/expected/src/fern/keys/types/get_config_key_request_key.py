

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetConfigKeyRequestKey(enum.StrEnum):
    PAGE_INFO = "pageInfo"
    APP_CONFIG = "appConfig"
    SECTIONS = "sections"
    PAGES = "pages"

    def visit(
        self,
        page_info: typing.Callable[[], T_Result],
        app_config: typing.Callable[[], T_Result],
        sections: typing.Callable[[], T_Result],
        pages: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetConfigKeyRequestKey.PAGE_INFO:
            return page_info()
        if self is GetConfigKeyRequestKey.APP_CONFIG:
            return app_config()
        if self is GetConfigKeyRequestKey.SECTIONS:
            return sections()
        if self is GetConfigKeyRequestKey.PAGES:
            return pages()
