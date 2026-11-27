

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntityLinkFormFieldType(enum.StrEnum):
    """
    The type of this form field. Type declares how this field behaves and dictates the additional properties passed along with the required properties like label and key
    """

    ENTITY_LINK = "ENTITY_LINK"

    def visit(self, entity_link: typing.Callable[[], T_Result]) -> T_Result:
        if self is EntityLinkFormFieldType.ENTITY_LINK:
            return entity_link()
