

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptDataTemplateFormat(enum.StrEnum):
    MUSTACHE = "mustache"
    NUNJUCKS = "nunjucks"
    NONE = "none"

    def visit(
        self,
        mustache: typing.Callable[[], T_Result],
        nunjucks: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PromptDataTemplateFormat.MUSTACHE:
            return mustache()
        if self is PromptDataTemplateFormat.NUNJUCKS:
            return nunjucks()
        if self is PromptDataTemplateFormat.NONE:
            return none()
