

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FourHundredFourDetailsItemDescription(enum.StrEnum):
    SPECIFIED_RESOURCE_ID_DOES_NOT_EXIST_PLEASE_CHECK_THE_RESOURCE_ID_AND_TRY_AGAIN = (
        "Specified resource ID does not exist. Please check the resource ID and try again."
    )

    def visit(
        self,
        specified_resource_id_does_not_exist_please_check_the_resource_id_and_try_again: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is FourHundredFourDetailsItemDescription.SPECIFIED_RESOURCE_ID_DOES_NOT_EXIST_PLEASE_CHECK_THE_RESOURCE_ID_AND_TRY_AGAIN
        ):
            return specified_resource_id_does_not_exist_please_check_the_resource_id_and_try_again()
