

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateSystemModelsAvailableSubscriptionSubscriptionType(enum.StrEnum):
    """
    The type of subscription supported.
    """

    REQUIRED = "Required"
    INCLUDE_BY_DEFAULT = "IncludeByDefault"
    EXCLUDE_BY_DEFAULT = "ExcludeByDefault"

    def visit(
        self,
        required: typing.Callable[[], T_Result],
        include_by_default: typing.Callable[[], T_Result],
        exclude_by_default: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateSystemModelsAvailableSubscriptionSubscriptionType.REQUIRED:
            return required()
        if self is UpdateSystemModelsAvailableSubscriptionSubscriptionType.INCLUDE_BY_DEFAULT:
            return include_by_default()
        if self is UpdateSystemModelsAvailableSubscriptionSubscriptionType.EXCLUDE_BY_DEFAULT:
            return exclude_by_default()
