

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFilterRequestTargetFilter(enum.StrEnum):
    MODULE = "module"
    CATEGORY = "category"
    RESOURCE_TYPE = "resourceType"

    def visit(
        self,
        module: typing.Callable[[], T_Result],
        category: typing.Callable[[], T_Result],
        resource_type: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetFilterRequestTargetFilter.MODULE:
            return module()
        if self is GetFilterRequestTargetFilter.CATEGORY:
            return category()
        if self is GetFilterRequestTargetFilter.RESOURCE_TYPE:
            return resource_type()
