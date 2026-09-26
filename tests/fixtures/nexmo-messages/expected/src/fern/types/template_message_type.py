

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TemplateMessageType(enum.StrEnum):
    """
    The type of message to send. You must provide `template` in this field
    """

    TEMPLATE = "template"

    def visit(self, template: typing.Callable[[], T_Result]) -> T_Result:
        if self is TemplateMessageType.TEMPLATE:
            return template()
