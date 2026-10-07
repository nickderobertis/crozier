

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RuntimeConfigDefaultAutoDownloadItem(enum.StrEnum):
    HTML = "html"
    IPYNB = "ipynb"
    MARKDOWN = "markdown"

    def visit(
        self,
        html: typing.Callable[[], T_Result],
        ipynb: typing.Callable[[], T_Result],
        markdown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RuntimeConfigDefaultAutoDownloadItem.HTML:
            return html()
        if self is RuntimeConfigDefaultAutoDownloadItem.IPYNB:
            return ipynb()
        if self is RuntimeConfigDefaultAutoDownloadItem.MARKDOWN:
            return markdown()
