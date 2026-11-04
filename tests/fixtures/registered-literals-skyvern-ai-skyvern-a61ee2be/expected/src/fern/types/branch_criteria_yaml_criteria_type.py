

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BranchCriteriaYamlCriteriaType(enum.StrEnum):
    JINJA2TEMPLATE = "jinja2_template"
    PROMPT = "prompt"

    def visit(self, jinja2template: typing.Callable[[], T_Result], prompt: typing.Callable[[], T_Result]) -> T_Result:
        if self is BranchCriteriaYamlCriteriaType.JINJA2TEMPLATE:
            return jinja2template()
        if self is BranchCriteriaYamlCriteriaType.PROMPT:
            return prompt()
