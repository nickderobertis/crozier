

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CollectionsSortBy(str, enum.Enum):
    """
    The field on which to sort the Collections
    """

    NAME = "name"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"

    def visit(
        self,
        name: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CollectionsSortBy.NAME:
            return name()
        if self is CollectionsSortBy.CREATED_AT:
            return created_at()
        if self is CollectionsSortBy.UPDATED_AT:
            return updated_at()
