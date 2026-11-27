

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntitySearchFormInstanceProviderType(enum.StrEnum):
    ENTITY_SEARCH = "ENTITY_SEARCH"

    def visit(self, entity_search: typing.Callable[[], T_Result]) -> T_Result:
        if self is EntitySearchFormInstanceProviderType.ENTITY_SEARCH:
            return entity_search()
