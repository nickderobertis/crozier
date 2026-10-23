

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetContactAttributeKeysRequestFilterDateField(enum.StrEnum):
    """
    Date field to filter by
    """

    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"

    def visit(self, created_at: typing.Callable[[], T_Result], updated_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetContactAttributeKeysRequestFilterDateField.CREATED_AT:
            return created_at()
        if self is GetContactAttributeKeysRequestFilterDateField.UPDATED_AT:
            return updated_at()
