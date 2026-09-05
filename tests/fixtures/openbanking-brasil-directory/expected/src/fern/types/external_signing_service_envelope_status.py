

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExternalSigningServiceEnvelopeStatus(enum.StrEnum):
    COMPLETED = "completed"
    CREATED = "created"
    DECLINED = "declined"
    DELETED = "deleted"
    DELIVERED = "delivered"
    PROCESSING = "processing"
    SENT = "sent"
    SIGNED = "signed"
    TEMPLATE = "template"
    VOIDED = "voided"
    EXPIRED = "expired"

    def visit(
        self,
        completed: typing.Callable[[], T_Result],
        created: typing.Callable[[], T_Result],
        declined: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        delivered: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        sent: typing.Callable[[], T_Result],
        signed: typing.Callable[[], T_Result],
        template: typing.Callable[[], T_Result],
        voided: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExternalSigningServiceEnvelopeStatus.COMPLETED:
            return completed()
        if self is ExternalSigningServiceEnvelopeStatus.CREATED:
            return created()
        if self is ExternalSigningServiceEnvelopeStatus.DECLINED:
            return declined()
        if self is ExternalSigningServiceEnvelopeStatus.DELETED:
            return deleted()
        if self is ExternalSigningServiceEnvelopeStatus.DELIVERED:
            return delivered()
        if self is ExternalSigningServiceEnvelopeStatus.PROCESSING:
            return processing()
        if self is ExternalSigningServiceEnvelopeStatus.SENT:
            return sent()
        if self is ExternalSigningServiceEnvelopeStatus.SIGNED:
            return signed()
        if self is ExternalSigningServiceEnvelopeStatus.TEMPLATE:
            return template()
        if self is ExternalSigningServiceEnvelopeStatus.VOIDED:
            return voided()
        if self is ExternalSigningServiceEnvelopeStatus.EXPIRED:
            return expired()
