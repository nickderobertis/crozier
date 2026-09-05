

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptDataNullishTemplateFormat(enum.StrEnum):
    MUSTACHE = "mustache"
    NUNJUCKS = "nunjucks"
    NONE = "none"

    def visit(
        self,
        mustache: typing.Callable[[], T_Result],
        nunjucks: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PromptDataNullishTemplateFormat.MUSTACHE:
            return mustache()
        if self is PromptDataNullishTemplateFormat.NUNJUCKS:
            return nunjucks()
        if self is PromptDataNullishTemplateFormat.NONE:
            return none()
