

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateApiKeyRequestScopesItem(enum.StrEnum):
    DIRECTORY_READ = "directory:read"

    def visit(self, directory_read: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateApiKeyRequestScopesItem.DIRECTORY_READ:
            return directory_read()
