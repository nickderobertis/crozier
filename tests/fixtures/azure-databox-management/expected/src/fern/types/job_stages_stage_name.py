

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobStagesStageName(enum.StrEnum):
    """
    Name of the job stage.
    """

    DEVICE_ORDERED = "DeviceOrdered"
    DEVICE_PREPARED = "DevicePrepared"
    DISPATCHED = "Dispatched"
    DELIVERED = "Delivered"
    PICKED_UP = "PickedUp"
    AT_AZURE_DC = "AtAzureDC"
    DATA_COPY = "DataCopy"
    COMPLETED = "Completed"
    COMPLETED_WITH_ERRORS = "CompletedWithErrors"
    CANCELLED = "Cancelled"
    FAILED_ISSUE_REPORTED_AT_CUSTOMER = "Failed_IssueReportedAtCustomer"
    FAILED_ISSUE_DETECTED_AT_AZURE_DC = "Failed_IssueDetectedAtAzureDC"
    ABORTED = "Aborted"
    COMPLETED_WITH_WARNINGS = "CompletedWithWarnings"
    READY_TO_DISPATCH_FROM_AZURE_DC = "ReadyToDispatchFromAzureDC"
    READY_TO_RECEIVE_AT_AZURE_DC = "ReadyToReceiveAtAzureDC"

    def visit(
        self,
        device_ordered: typing.Callable[[], T_Result],
        device_prepared: typing.Callable[[], T_Result],
        dispatched: typing.Callable[[], T_Result],
        delivered: typing.Callable[[], T_Result],
        picked_up: typing.Callable[[], T_Result],
        at_azure_dc: typing.Callable[[], T_Result],
        data_copy: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        completed_with_errors: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        failed_issue_reported_at_customer: typing.Callable[[], T_Result],
        failed_issue_detected_at_azure_dc: typing.Callable[[], T_Result],
        aborted: typing.Callable[[], T_Result],
        completed_with_warnings: typing.Callable[[], T_Result],
        ready_to_dispatch_from_azure_dc: typing.Callable[[], T_Result],
        ready_to_receive_at_azure_dc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobStagesStageName.DEVICE_ORDERED:
            return device_ordered()
        if self is JobStagesStageName.DEVICE_PREPARED:
            return device_prepared()
        if self is JobStagesStageName.DISPATCHED:
            return dispatched()
        if self is JobStagesStageName.DELIVERED:
            return delivered()
        if self is JobStagesStageName.PICKED_UP:
            return picked_up()
        if self is JobStagesStageName.AT_AZURE_DC:
            return at_azure_dc()
        if self is JobStagesStageName.DATA_COPY:
            return data_copy()
        if self is JobStagesStageName.COMPLETED:
            return completed()
        if self is JobStagesStageName.COMPLETED_WITH_ERRORS:
            return completed_with_errors()
        if self is JobStagesStageName.CANCELLED:
            return cancelled()
        if self is JobStagesStageName.FAILED_ISSUE_REPORTED_AT_CUSTOMER:
            return failed_issue_reported_at_customer()
        if self is JobStagesStageName.FAILED_ISSUE_DETECTED_AT_AZURE_DC:
            return failed_issue_detected_at_azure_dc()
        if self is JobStagesStageName.ABORTED:
            return aborted()
        if self is JobStagesStageName.COMPLETED_WITH_WARNINGS:
            return completed_with_warnings()
        if self is JobStagesStageName.READY_TO_DISPATCH_FROM_AZURE_DC:
            return ready_to_dispatch_from_azure_dc()
        if self is JobStagesStageName.READY_TO_RECEIVE_AT_AZURE_DC:
            return ready_to_receive_at_azure_dc()
