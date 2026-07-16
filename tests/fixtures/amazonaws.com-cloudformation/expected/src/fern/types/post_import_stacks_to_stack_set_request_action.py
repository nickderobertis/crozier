

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostImportStacksToStackSetRequestAction(enum.StrEnum):
    IMPORT_STACKS_TO_STACK_SET = "ImportStacksToStackSet"

    def visit(self, import_stacks_to_stack_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostImportStacksToStackSetRequestAction.IMPORT_STACKS_TO_STACK_SET:
            return import_stacks_to_stack_set()
