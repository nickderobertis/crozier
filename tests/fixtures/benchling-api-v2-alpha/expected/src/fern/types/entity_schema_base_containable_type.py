

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntitySchemaBaseContainableType(enum.StrEnum):
    NONE = "NONE"
    ENTITY = "ENTITY"
    BATCH = "BATCH"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        entity: typing.Callable[[], T_Result],
        batch: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntitySchemaBaseContainableType.NONE:
            return none()
        if self is EntitySchemaBaseContainableType.ENTITY:
            return entity()
        if self is EntitySchemaBaseContainableType.BATCH:
            return batch()
