

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType(enum.StrEnum):
    """
    Optional. The type of subscription supported.  The default subscription type is Required.
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
        if self is UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType.REQUIRED:
            return required()
        if self is UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType.INCLUDE_BY_DEFAULT:
            return include_by_default()
        if self is UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType.EXCLUDE_BY_DEFAULT:
            return exclude_by_default()
