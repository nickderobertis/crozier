

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VocabularyTermAppliesItem(enum.StrEnum):
    SCHEME = "scheme"
    ORGANIZATION = "organization"
    TOOL = "tool"
    MAPPING = "mapping"
    ENDORSEMENT = "endorsement"

    def visit(
        self,
        scheme: typing.Callable[[], T_Result],
        organization: typing.Callable[[], T_Result],
        tool: typing.Callable[[], T_Result],
        mapping: typing.Callable[[], T_Result],
        endorsement: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VocabularyTermAppliesItem.SCHEME:
            return scheme()
        if self is VocabularyTermAppliesItem.ORGANIZATION:
            return organization()
        if self is VocabularyTermAppliesItem.TOOL:
            return tool()
        if self is VocabularyTermAppliesItem.MAPPING:
            return mapping()
        if self is VocabularyTermAppliesItem.ENDORSEMENT:
            return endorsement()
