

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetValidateTemplateRequestAction(str, enum.Enum):
    VALIDATE_TEMPLATE = "ValidateTemplate"

    def visit(self, validate_template: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetValidateTemplateRequestAction.VALIDATE_TEMPLATE:
            return validate_template()
