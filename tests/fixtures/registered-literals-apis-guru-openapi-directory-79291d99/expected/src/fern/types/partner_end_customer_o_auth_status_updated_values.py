

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PartnerEndCustomerOAuthStatusUpdatedValues(enum.StrEnum):
    """
    The OAuth status of the update
    """

    NOT_STARTED = "not-started"
    PROCESSING = "processing"
    APPROVED = "approved"
    ENABLED = "enabled"
    ATTENTION_REQUIRED = "attention-required"

    def visit(
        self,
        not_started: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        enabled: typing.Callable[[], T_Result],
        attention_required: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PartnerEndCustomerOAuthStatusUpdatedValues.NOT_STARTED:
            return not_started()
        if self is PartnerEndCustomerOAuthStatusUpdatedValues.PROCESSING:
            return processing()
        if self is PartnerEndCustomerOAuthStatusUpdatedValues.APPROVED:
            return approved()
        if self is PartnerEndCustomerOAuthStatusUpdatedValues.ENABLED:
            return enabled()
        if self is PartnerEndCustomerOAuthStatusUpdatedValues.ATTENTION_REQUIRED:
            return attention_required()
