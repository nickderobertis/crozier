

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetImportStacksToStackSetRequestAction(str, enum.Enum):
    IMPORT_STACKS_TO_STACK_SET = "ImportStacksToStackSet"

    def visit(self, import_stacks_to_stack_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetImportStacksToStackSetRequestAction.IMPORT_STACKS_TO_STACK_SET:
            return import_stacks_to_stack_set()
