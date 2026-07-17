

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectorDocFormat(enum.StrEnum):
    """
    Format of the doc.
    """

    MARKDOWN = "markdown"

    def visit(self, markdown: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectorDocFormat.MARKDOWN:
            return markdown()
