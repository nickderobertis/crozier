

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LeadEventType(enum.StrEnum):
    ALL = "*"
    LEAD_LEAD_CREATED = "lead.lead.created"
    LEAD_LEAD_UPDATED = "lead.lead.updated"
    LEAD_LEAD_DELETED = "lead.lead.deleted"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        lead_lead_created: typing.Callable[[], T_Result],
        lead_lead_updated: typing.Callable[[], T_Result],
        lead_lead_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LeadEventType.ALL:
            return all_()
        if self is LeadEventType.LEAD_LEAD_CREATED:
            return lead_lead_created()
        if self is LeadEventType.LEAD_LEAD_UPDATED:
            return lead_lead_updated()
        if self is LeadEventType.LEAD_LEAD_DELETED:
            return lead_lead_deleted()
