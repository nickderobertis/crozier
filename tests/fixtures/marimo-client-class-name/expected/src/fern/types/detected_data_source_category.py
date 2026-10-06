

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetectedDataSourceCategory(enum.StrEnum):
    CATALOG = "catalog"
    DATABASE = "database"
    OBJECT_STORAGE = "object-storage"

    def visit(
        self,
        catalog: typing.Callable[[], T_Result],
        database: typing.Callable[[], T_Result],
        object_storage: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DetectedDataSourceCategory.CATALOG:
            return catalog()
        if self is DetectedDataSourceCategory.DATABASE:
            return database()
        if self is DetectedDataSourceCategory.OBJECT_STORAGE:
            return object_storage()
