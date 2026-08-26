

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppConfigAutoDownloadItem(enum.StrEnum):
    HTML = "html"
    IPYNB = "ipynb"
    MARKDOWN = "markdown"

    def visit(
        self,
        html: typing.Callable[[], T_Result],
        ipynb: typing.Callable[[], T_Result],
        markdown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppConfigAutoDownloadItem.HTML:
            return html()
        if self is AppConfigAutoDownloadItem.IPYNB:
            return ipynb()
        if self is AppConfigAutoDownloadItem.MARKDOWN:
            return markdown()
