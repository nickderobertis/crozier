

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FourHundredThreeDetailsItemDescription(enum.StrEnum):
    YOU_DO_NOT_HAVE_PERMISSION_TO_ACCESS_OR_PERFORM_OPERATIONS_ON_THIS_RESOURCE = (
        "You do not have permission to access or perform operations on this resource."
    )

    def visit(
        self, you_do_not_have_permission_to_access_or_perform_operations_on_this_resource: typing.Callable[[], T_Result]
    ) -> T_Result:
        if (
            self
            is FourHundredThreeDetailsItemDescription.YOU_DO_NOT_HAVE_PERMISSION_TO_ACCESS_OR_PERFORM_OPERATIONS_ON_THIS_RESOURCE
        ):
            return you_do_not_have_permission_to_access_or_perform_operations_on_this_resource()
