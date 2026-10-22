

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApiKeyObject(enum.StrEnum):
    """
    Object type identifier
    """

    API_KEY = "api_key"

    def visit(self, api_key: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApiKeyObject.API_KEY:
            return api_key()
