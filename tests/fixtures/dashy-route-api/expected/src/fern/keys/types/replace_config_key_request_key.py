

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ReplaceConfigKeyRequestKey(enum.StrEnum):
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
        if self is ReplaceConfigKeyRequestKey.PAGE_INFO:
            return page_info()
        if self is ReplaceConfigKeyRequestKey.APP_CONFIG:
            return app_config()
        if self is ReplaceConfigKeyRequestKey.SECTIONS:
            return sections()
        if self is ReplaceConfigKeyRequestKey.PAGES:
            return pages()
