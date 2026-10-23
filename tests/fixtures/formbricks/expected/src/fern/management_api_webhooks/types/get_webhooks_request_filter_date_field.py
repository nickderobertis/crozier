

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWebhooksRequestFilterDateField(enum.StrEnum):
    """
    Date field to filter by
    """

    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"

    def visit(self, created_at: typing.Callable[[], T_Result], updated_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetWebhooksRequestFilterDateField.CREATED_AT:
            return created_at()
        if self is GetWebhooksRequestFilterDateField.UPDATED_AT:
            return updated_at()
