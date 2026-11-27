

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class EntitySchemaCreateContainableType(enum.StrEnum):
    NONE = "NONE"
    ENTITY = "ENTITY"
    BATCH = "BATCH"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        entity: typing.Callable[[], T_Result],
        batch: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntitySchemaCreateContainableType.NONE:
            return none()
        if self is EntitySchemaCreateContainableType.ENTITY:
            return entity()
        if self is EntitySchemaCreateContainableType.BATCH:
            return batch()
