

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PartnerEndCustomerQuestionnaireStatus(enum.StrEnum):
    """
    The status of the end customer's security questionnaire.
    """

    NOT_STARTED = "NOT_STARTED"
    RECEIVED = "RECEIVED"
    COMPLETE = "COMPLETE"

    def visit(
        self,
        not_started: typing.Callable[[], T_Result],
        received: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PartnerEndCustomerQuestionnaireStatus.NOT_STARTED:
            return not_started()
        if self is PartnerEndCustomerQuestionnaireStatus.RECEIVED:
            return received()
        if self is PartnerEndCustomerQuestionnaireStatus.COMPLETE:
            return complete()
