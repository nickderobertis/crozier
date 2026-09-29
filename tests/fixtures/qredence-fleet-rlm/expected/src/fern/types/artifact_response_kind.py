

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ArtifactResponseKind(enum.StrEnum):
    TEXT = "text"
    MARKDOWN = "markdown"
    JSON = "json"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        markdown: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ArtifactResponseKind.TEXT:
            return text()
        if self is ArtifactResponseKind.MARKDOWN:
            return markdown()
        if self is ArtifactResponseKind.JSON:
            return json()
