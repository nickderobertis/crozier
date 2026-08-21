

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeletionDeniedReason(enum.StrEnum):
    """
    A justification for why a deletion request could not be completely or partially complied to.
    """

    FREEDOM_OF_EXPRESSION = "freedom_of_expression"
    LEGAL_OBLIGATION = "legal_obligation"
    PUBLIC_HEALTH_INTEREST = "public_health_interest"
    ARCHIVAL = "archival"
    LEGAL_CLAIMS = "legal_claims"
    NO_PERSONAL_DATA_TO_DELETE = "no_personal_data_to_delete"
    NO_GROUNDS_FOR_DELETION_REQUEST = "no_grounds_for_deletion_request"

    def visit(
        self,
        freedom_of_expression: typing.Callable[[], T_Result],
        legal_obligation: typing.Callable[[], T_Result],
        public_health_interest: typing.Callable[[], T_Result],
        archival: typing.Callable[[], T_Result],
        legal_claims: typing.Callable[[], T_Result],
        no_personal_data_to_delete: typing.Callable[[], T_Result],
        no_grounds_for_deletion_request: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeletionDeniedReason.FREEDOM_OF_EXPRESSION:
            return freedom_of_expression()
        if self is DeletionDeniedReason.LEGAL_OBLIGATION:
            return legal_obligation()
        if self is DeletionDeniedReason.PUBLIC_HEALTH_INTEREST:
            return public_health_interest()
        if self is DeletionDeniedReason.ARCHIVAL:
            return archival()
        if self is DeletionDeniedReason.LEGAL_CLAIMS:
            return legal_claims()
        if self is DeletionDeniedReason.NO_PERSONAL_DATA_TO_DELETE:
            return no_personal_data_to_delete()
        if self is DeletionDeniedReason.NO_GROUNDS_FOR_DELETION_REQUEST:
            return no_grounds_for_deletion_request()
