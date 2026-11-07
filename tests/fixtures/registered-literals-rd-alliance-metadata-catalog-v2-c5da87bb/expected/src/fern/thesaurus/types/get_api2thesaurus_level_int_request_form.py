

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApi2ThesaurusLevelIntRequestForm(enum.StrEnum):
    CONCEPT = "concept"
    TREE = "tree"

    def visit(self, concept: typing.Callable[[], T_Result], tree: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetApi2ThesaurusLevelIntRequestForm.CONCEPT:
            return concept()
        if self is GetApi2ThesaurusLevelIntRequestForm.TREE:
            return tree()
