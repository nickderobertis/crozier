

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostValidateTemplateRequestAction(enum.StrEnum):
    VALIDATE_TEMPLATE = "ValidateTemplate"

    def visit(self, validate_template: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostValidateTemplateRequestAction.VALIDATE_TEMPLATE:
            return validate_template()
