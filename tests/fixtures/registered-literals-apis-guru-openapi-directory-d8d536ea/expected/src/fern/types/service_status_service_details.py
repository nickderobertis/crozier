

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceStatusServiceDetails(enum.StrEnum):
    """
    Status Details of Case Update Services Status.
    """

    ACCEPTING_CASE_UPDATES = "acceptingCaseUpdates"
    NOT_ACCEPTING_CASE_UPDATES = "notAcceptingCaseUpdates"
    ACCEPTING_CASE_TRACK = "acceptingCaseTrack"
    NOT_ACCEPTING_CASE_TRACK = "notAcceptingCaseTrack"
    ACCEPTING_AUTO_DOC_ORDERS = "acceptingAutoDocOrders"
    ACCEPTING_MANUAL_DOC_ORDERS = "acceptingManualDocOrders"
    NOT_ACCEPTING_AUTO_DOC_ORDERS_LIMIT_EXCEEDED = "notAcceptingAutoDocOrdersLimitExceeded"
    NOT_ACCEPTING_MANUAL_DOC_ORDERS_LIMIT_EXCEEDED = "notAcceptingManualDocOrdersLimitExceeded"
    NOT_ACCEPTING_DOC_ORDERS = "notAcceptingDocOrders"

    def visit(
        self,
        accepting_case_updates: typing.Callable[[], T_Result],
        not_accepting_case_updates: typing.Callable[[], T_Result],
        accepting_case_track: typing.Callable[[], T_Result],
        not_accepting_case_track: typing.Callable[[], T_Result],
        accepting_auto_doc_orders: typing.Callable[[], T_Result],
        accepting_manual_doc_orders: typing.Callable[[], T_Result],
        not_accepting_auto_doc_orders_limit_exceeded: typing.Callable[[], T_Result],
        not_accepting_manual_doc_orders_limit_exceeded: typing.Callable[[], T_Result],
        not_accepting_doc_orders: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceStatusServiceDetails.ACCEPTING_CASE_UPDATES:
            return accepting_case_updates()
        if self is ServiceStatusServiceDetails.NOT_ACCEPTING_CASE_UPDATES:
            return not_accepting_case_updates()
        if self is ServiceStatusServiceDetails.ACCEPTING_CASE_TRACK:
            return accepting_case_track()
        if self is ServiceStatusServiceDetails.NOT_ACCEPTING_CASE_TRACK:
            return not_accepting_case_track()
        if self is ServiceStatusServiceDetails.ACCEPTING_AUTO_DOC_ORDERS:
            return accepting_auto_doc_orders()
        if self is ServiceStatusServiceDetails.ACCEPTING_MANUAL_DOC_ORDERS:
            return accepting_manual_doc_orders()
        if self is ServiceStatusServiceDetails.NOT_ACCEPTING_AUTO_DOC_ORDERS_LIMIT_EXCEEDED:
            return not_accepting_auto_doc_orders_limit_exceeded()
        if self is ServiceStatusServiceDetails.NOT_ACCEPTING_MANUAL_DOC_ORDERS_LIMIT_EXCEEDED:
            return not_accepting_manual_doc_orders_limit_exceeded()
        if self is ServiceStatusServiceDetails.NOT_ACCEPTING_DOC_ORDERS:
            return not_accepting_doc_orders()
