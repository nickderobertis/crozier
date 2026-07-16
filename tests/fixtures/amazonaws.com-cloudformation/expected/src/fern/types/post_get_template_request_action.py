

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostGetTemplateRequestAction(str, enum.Enum):
    GET_TEMPLATE = "GetTemplate"

    def visit(self, get_template: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostGetTemplateRequestAction.GET_TEMPLATE:
            return get_template()
