

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PrebuiltWorkflowStepName(enum.StrEnum):
    """
    Workflow to run — doubles as the result key in ``output``. v1 only: ``"parse-extract"``.
    """

    PARSE_EXTRACT = "parse-extract"

    def visit(self, parse_extract: typing.Callable[[], T_Result]) -> T_Result:
        if self is PrebuiltWorkflowStepName.PARSE_EXTRACT:
            return parse_extract()
