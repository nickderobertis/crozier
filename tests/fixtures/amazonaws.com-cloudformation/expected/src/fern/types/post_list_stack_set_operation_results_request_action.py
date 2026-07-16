

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostListStackSetOperationResultsRequestAction(str, enum.Enum):
    LIST_STACK_SET_OPERATION_RESULTS = "ListStackSetOperationResults"

    def visit(self, list_stack_set_operation_results: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostListStackSetOperationResultsRequestAction.LIST_STACK_SET_OPERATION_RESULTS:
            return list_stack_set_operation_results()
