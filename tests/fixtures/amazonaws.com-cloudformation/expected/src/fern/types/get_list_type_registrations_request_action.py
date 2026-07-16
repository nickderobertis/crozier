

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetListTypeRegistrationsRequestAction(enum.StrEnum):
    LIST_TYPE_REGISTRATIONS = "ListTypeRegistrations"

    def visit(self, list_type_registrations: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListTypeRegistrationsRequestAction.LIST_TYPE_REGISTRATIONS:
            return list_type_registrations()
