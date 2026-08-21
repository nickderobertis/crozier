

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeletionRequestGrounds(enum.StrEnum):
    """
    The data subject's reason for her personal data deletion request.
    """

    NO_LONGER_NECESSARY = "no_longer_necessary"
    CONSENT_WITHDRAWN = "consent_withdrawn"
    OBJECTION_TO_PROCESSING = "objection_to_processing"
    PROCESSING_UNLAWFUL = "processing_unlawful"
    LEGAL_COMPLIANCE = "legal_compliance"
    UNDERAGE_DATA_SUBJECT = "underage_data_subject"
    UNSPECIFIED = "unspecified"

    def visit(
        self,
        no_longer_necessary: typing.Callable[[], T_Result],
        consent_withdrawn: typing.Callable[[], T_Result],
        objection_to_processing: typing.Callable[[], T_Result],
        processing_unlawful: typing.Callable[[], T_Result],
        legal_compliance: typing.Callable[[], T_Result],
        underage_data_subject: typing.Callable[[], T_Result],
        unspecified: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeletionRequestGrounds.NO_LONGER_NECESSARY:
            return no_longer_necessary()
        if self is DeletionRequestGrounds.CONSENT_WITHDRAWN:
            return consent_withdrawn()
        if self is DeletionRequestGrounds.OBJECTION_TO_PROCESSING:
            return objection_to_processing()
        if self is DeletionRequestGrounds.PROCESSING_UNLAWFUL:
            return processing_unlawful()
        if self is DeletionRequestGrounds.LEGAL_COMPLIANCE:
            return legal_compliance()
        if self is DeletionRequestGrounds.UNDERAGE_DATA_SUBJECT:
            return underage_data_subject()
        if self is DeletionRequestGrounds.UNSPECIFIED:
            return unspecified()
