

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntityLinkFormFieldEntityType(enum.StrEnum):
    """
    Benchling entity type of this link. Currently only custom_entity is supported
    """

    CUSTOM_ENTITY = "custom_entity"

    def visit(self, custom_entity: typing.Callable[[], T_Result]) -> T_Result:
        if self is EntityLinkFormFieldEntityType.CUSTOM_ENTITY:
            return custom_entity()
