

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error422Message(enum.StrEnum):
    THE_REQUESTED_ACTION_COULD_NOT_BE_PERFORMED_SEMANTICALLY_INCORRECT_OR_FAILED_BUSINESS_VALIDATION = (
        "The requested action could not be performed, semantically incorrect, or failed business validation."
    )

    def visit(
        self,
        the_requested_action_could_not_be_performed_semantically_incorrect_or_failed_business_validation: typing.Callable[
            [], T_Result
        ],
    ) -> T_Result:
        if (
            self
            is Error422Message.THE_REQUESTED_ACTION_COULD_NOT_BE_PERFORMED_SEMANTICALLY_INCORRECT_OR_FAILED_BUSINESS_VALIDATION
        ):
            return the_requested_action_could_not_be_performed_semantically_incorrect_or_failed_business_validation()
