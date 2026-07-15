

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectorDocFormat(str, enum.Enum):
    """
    Format of the doc.
    """

    MARKDOWN = "markdown"

    def visit(self, markdown: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectorDocFormat.MARKDOWN:
            return markdown()
