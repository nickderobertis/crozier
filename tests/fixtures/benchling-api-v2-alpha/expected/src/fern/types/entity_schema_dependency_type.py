

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntitySchemaDependencyType(enum.StrEnum):
    ENTITY_SCHEMA = "entity_schema"

    def visit(self, entity_schema: typing.Callable[[], T_Result]) -> T_Result:
        if self is EntitySchemaDependencyType.ENTITY_SCHEMA:
            return entity_schema()
