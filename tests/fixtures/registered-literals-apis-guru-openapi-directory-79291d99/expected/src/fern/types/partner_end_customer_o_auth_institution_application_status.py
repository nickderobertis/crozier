

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PartnerEndCustomerOAuthInstitutionApplicationStatus(enum.StrEnum):
    """
    The registration status for the end customer's application.
    """

    NOT_STARTED = "NOT_STARTED"
    PROCESSING = "PROCESSING"
    APPROVED = "APPROVED"
    ENABLED = "ENABLED"
    ATTENTION_REQUIRED = "ATTENTION_REQUIRED"

    def visit(
        self,
        not_started: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        enabled: typing.Callable[[], T_Result],
        attention_required: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PartnerEndCustomerOAuthInstitutionApplicationStatus.NOT_STARTED:
            return not_started()
        if self is PartnerEndCustomerOAuthInstitutionApplicationStatus.PROCESSING:
            return processing()
        if self is PartnerEndCustomerOAuthInstitutionApplicationStatus.APPROVED:
            return approved()
        if self is PartnerEndCustomerOAuthInstitutionApplicationStatus.ENABLED:
            return enabled()
        if self is PartnerEndCustomerOAuthInstitutionApplicationStatus.ATTENTION_REQUIRED:
            return attention_required()
