

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineListWorkflowsResponseItemsItemTag(enum.StrEnum):
    """
    Tag used for the workflow
    """

    SETUP = "setup"

    def visit(self, setup: typing.Callable[[], T_Result]) -> T_Result:
        if self is PipelineListWorkflowsResponseItemsItemTag.SETUP:
            return setup()
