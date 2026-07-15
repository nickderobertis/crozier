

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LeadsSortBy(str, enum.Enum):
    """
    The field on which to sort the Leads
    """

    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    NAME = "name"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    EMAIL = "email"

    def visit(
        self,
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        first_name: typing.Callable[[], T_Result],
        last_name: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LeadsSortBy.CREATED_AT:
            return created_at()
        if self is LeadsSortBy.UPDATED_AT:
            return updated_at()
        if self is LeadsSortBy.NAME:
            return name()
        if self is LeadsSortBy.FIRST_NAME:
            return first_name()
        if self is LeadsSortBy.LAST_NAME:
            return last_name()
        if self is LeadsSortBy.EMAIL:
            return email()
