

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SourceDefinitionReadSourceType(str, enum.Enum):
    API = "api"
    FILE = "file"
    DATABASE = "database"
    CUSTOM = "custom"

    def visit(
        self,
        api: typing.Callable[[], T_Result],
        file: typing.Callable[[], T_Result],
        database: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SourceDefinitionReadSourceType.API:
            return api()
        if self is SourceDefinitionReadSourceType.FILE:
            return file()
        if self is SourceDefinitionReadSourceType.DATABASE:
            return database()
        if self is SourceDefinitionReadSourceType.CUSTOM:
            return custom()
