

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AiTranslateSurveyRequestRunStrategy(enum.StrEnum):
    SKIP_EXIST = "skipExist"
    REBUILD_ALL = "rebuildAll"

    def visit(self, skip_exist: typing.Callable[[], T_Result], rebuild_all: typing.Callable[[], T_Result]) -> T_Result:
        if self is AiTranslateSurveyRequestRunStrategy.SKIP_EXIST:
            return skip_exist()
        if self is AiTranslateSurveyRequestRunStrategy.REBUILD_ALL:
            return rebuild_all()
