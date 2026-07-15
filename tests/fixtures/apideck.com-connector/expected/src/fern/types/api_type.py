

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ApiType(str, enum.Enum):
    """
    Indicates whether the API is a Unified API. If unified_api is false, the API is a Platform API.
    """

    PLATFORM = "platform"
    UNIFIED = "unified"

    def visit(self, platform: typing.Callable[[], T_Result], unified: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApiType.PLATFORM:
            return platform()
        if self is ApiType.UNIFIED:
            return unified()
