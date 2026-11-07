

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AiClassifySurveyRequestRunStrategy(enum.StrEnum):
    SKIP_EXIST = "skipExist"
    SKIP_IN_SUGGEST = "skipInSuggest"
    REBUILD_ALL = "rebuildAll"

    def visit(
        self,
        skip_exist: typing.Callable[[], T_Result],
        skip_in_suggest: typing.Callable[[], T_Result],
        rebuild_all: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AiClassifySurveyRequestRunStrategy.SKIP_EXIST:
            return skip_exist()
        if self is AiClassifySurveyRequestRunStrategy.SKIP_IN_SUGGEST:
            return skip_in_suggest()
        if self is AiClassifySurveyRequestRunStrategy.REBUILD_ALL:
            return rebuild_all()
