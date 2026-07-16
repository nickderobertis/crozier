

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DisputeEvidenceType(str, enum.Enum):
    """
    The type of the dispute evidence.
    """

    GENERIC_EVIDENCE = "GENERIC_EVIDENCE"
    ONLINE_OR_APP_ACCESS_LOG = "ONLINE_OR_APP_ACCESS_LOG"
    AUTHORIZATION_DOCUMENTATION = "AUTHORIZATION_DOCUMENTATION"
    CANCELLATION_OR_REFUND_DOCUMENTATION = "CANCELLATION_OR_REFUND_DOCUMENTATION"
    CARDHOLDER_COMMUNICATION = "CARDHOLDER_COMMUNICATION"
    CARDHOLDER_INFORMATION = "CARDHOLDER_INFORMATION"
    PURCHASE_ACKNOWLEDGEMENT = "PURCHASE_ACKNOWLEDGEMENT"
    DUPLICATE_CHARGE_DOCUMENTATION = "DUPLICATE_CHARGE_DOCUMENTATION"
    PRODUCT_OR_SERVICE_DESCRIPTION = "PRODUCT_OR_SERVICE_DESCRIPTION"
    RECEIPT = "RECEIPT"
    SERVICE_RECEIVED_DOCUMENTATION = "SERVICE_RECEIVED_DOCUMENTATION"
    PROOF_OF_DELIVERY_DOCUMENTATION = "PROOF_OF_DELIVERY_DOCUMENTATION"
    RELATED_TRANSACTION_DOCUMENTATION = "RELATED_TRANSACTION_DOCUMENTATION"
    REBUTTAL_EXPLANATION = "REBUTTAL_EXPLANATION"
    TRACKING_NUMBER = "TRACKING_NUMBER"

    def visit(
        self,
        generic_evidence: typing.Callable[[], T_Result],
        online_or_app_access_log: typing.Callable[[], T_Result],
        authorization_documentation: typing.Callable[[], T_Result],
        cancellation_or_refund_documentation: typing.Callable[[], T_Result],
        cardholder_communication: typing.Callable[[], T_Result],
        cardholder_information: typing.Callable[[], T_Result],
        purchase_acknowledgement: typing.Callable[[], T_Result],
        duplicate_charge_documentation: typing.Callable[[], T_Result],
        product_or_service_description: typing.Callable[[], T_Result],
        receipt: typing.Callable[[], T_Result],
        service_received_documentation: typing.Callable[[], T_Result],
        proof_of_delivery_documentation: typing.Callable[[], T_Result],
        related_transaction_documentation: typing.Callable[[], T_Result],
        rebuttal_explanation: typing.Callable[[], T_Result],
        tracking_number: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DisputeEvidenceType.GENERIC_EVIDENCE:
            return generic_evidence()
        if self is DisputeEvidenceType.ONLINE_OR_APP_ACCESS_LOG:
            return online_or_app_access_log()
        if self is DisputeEvidenceType.AUTHORIZATION_DOCUMENTATION:
            return authorization_documentation()
        if self is DisputeEvidenceType.CANCELLATION_OR_REFUND_DOCUMENTATION:
            return cancellation_or_refund_documentation()
        if self is DisputeEvidenceType.CARDHOLDER_COMMUNICATION:
            return cardholder_communication()
        if self is DisputeEvidenceType.CARDHOLDER_INFORMATION:
            return cardholder_information()
        if self is DisputeEvidenceType.PURCHASE_ACKNOWLEDGEMENT:
            return purchase_acknowledgement()
        if self is DisputeEvidenceType.DUPLICATE_CHARGE_DOCUMENTATION:
            return duplicate_charge_documentation()
        if self is DisputeEvidenceType.PRODUCT_OR_SERVICE_DESCRIPTION:
            return product_or_service_description()
        if self is DisputeEvidenceType.RECEIPT:
            return receipt()
        if self is DisputeEvidenceType.SERVICE_RECEIVED_DOCUMENTATION:
            return service_received_documentation()
        if self is DisputeEvidenceType.PROOF_OF_DELIVERY_DOCUMENTATION:
            return proof_of_delivery_documentation()
        if self is DisputeEvidenceType.RELATED_TRANSACTION_DOCUMENTATION:
            return related_transaction_documentation()
        if self is DisputeEvidenceType.REBUTTAL_EXPLANATION:
            return rebuttal_explanation()
        if self is DisputeEvidenceType.TRACKING_NUMBER:
            return tracking_number()
