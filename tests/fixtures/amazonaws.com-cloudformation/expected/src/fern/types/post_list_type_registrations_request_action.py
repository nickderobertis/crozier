

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostListTypeRegistrationsRequestAction(str, enum.Enum):
    LIST_TYPE_REGISTRATIONS = "ListTypeRegistrations"

    def visit(self, list_type_registrations: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostListTypeRegistrationsRequestAction.LIST_TYPE_REGISTRATIONS:
            return list_type_registrations()
