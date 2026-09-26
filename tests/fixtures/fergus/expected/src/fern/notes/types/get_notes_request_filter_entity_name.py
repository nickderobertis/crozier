

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetNotesRequestFilterEntityName(enum.StrEnum):
    JOB = "JOB"
    CUSTOMER = "CUSTOMER"
    CUSTOMER_INVOICE = "CUSTOMER_INVOICE"
    QUOTE = "QUOTE"
    SITE = "SITE"
    TASK = "TASK"
    ENQUIRY = "ENQUIRY"
    JOB_PHASE = "JOB_PHASE"

    def visit(
        self,
        job: typing.Callable[[], T_Result],
        customer: typing.Callable[[], T_Result],
        customer_invoice: typing.Callable[[], T_Result],
        quote: typing.Callable[[], T_Result],
        site: typing.Callable[[], T_Result],
        task: typing.Callable[[], T_Result],
        enquiry: typing.Callable[[], T_Result],
        job_phase: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetNotesRequestFilterEntityName.JOB:
            return job()
        if self is GetNotesRequestFilterEntityName.CUSTOMER:
            return customer()
        if self is GetNotesRequestFilterEntityName.CUSTOMER_INVOICE:
            return customer_invoice()
        if self is GetNotesRequestFilterEntityName.QUOTE:
            return quote()
        if self is GetNotesRequestFilterEntityName.SITE:
            return site()
        if self is GetNotesRequestFilterEntityName.TASK:
            return task()
        if self is GetNotesRequestFilterEntityName.ENQUIRY:
            return enquiry()
        if self is GetNotesRequestFilterEntityName.JOB_PHASE:
            return job_phase()
