

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetListTypeVersionsRequestAction(str, enum.Enum):
    LIST_TYPE_VERSIONS = "ListTypeVersions"

    def visit(self, list_type_versions: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListTypeVersionsRequestAction.LIST_TYPE_VERSIONS:
            return list_type_versions()
