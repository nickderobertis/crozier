

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetListTypeVersionsRequestAction(enum.StrEnum):
    LIST_TYPE_VERSIONS = "ListTypeVersions"

    def visit(self, list_type_versions: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListTypeVersionsRequestAction.LIST_TYPE_VERSIONS:
            return list_type_versions()
