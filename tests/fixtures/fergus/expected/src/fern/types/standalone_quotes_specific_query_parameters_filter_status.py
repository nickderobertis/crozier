

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StandaloneQuotesSpecificQueryParametersFilterStatus(enum.StrEnum):
    DRAFT = "draft"
    ACCEPTED = "accepted"
    VOIDED = "voided"
    SUPERSEDED = "superseded"
    DECLINED = "declined"
    PUBLISHED = "published"
    EMAIL_SENT = "emailSent"
    EMAIL_NOT_SENT = "emailNotSent"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        accepted: typing.Callable[[], T_Result],
        voided: typing.Callable[[], T_Result],
        superseded: typing.Callable[[], T_Result],
        declined: typing.Callable[[], T_Result],
        published: typing.Callable[[], T_Result],
        email_sent: typing.Callable[[], T_Result],
        email_not_sent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StandaloneQuotesSpecificQueryParametersFilterStatus.DRAFT:
            return draft()
        if self is StandaloneQuotesSpecificQueryParametersFilterStatus.ACCEPTED:
            return accepted()
        if self is StandaloneQuotesSpecificQueryParametersFilterStatus.VOIDED:
            return voided()
        if self is StandaloneQuotesSpecificQueryParametersFilterStatus.SUPERSEDED:
            return superseded()
        if self is StandaloneQuotesSpecificQueryParametersFilterStatus.DECLINED:
            return declined()
        if self is StandaloneQuotesSpecificQueryParametersFilterStatus.PUBLISHED:
            return published()
        if self is StandaloneQuotesSpecificQueryParametersFilterStatus.EMAIL_SENT:
            return email_sent()
        if self is StandaloneQuotesSpecificQueryParametersFilterStatus.EMAIL_NOT_SENT:
            return email_not_sent()
