

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CrmEventType(str, enum.Enum):
    ALL = "*"
    CRM_ACTIVITY_CREATED = "crm.activity.created"
    CRM_ACTIVITY_UPDATED = "crm.activity.updated"
    CRM_ACTIVITY_DELETED = "crm.activity.deleted"
    CRM_COMPANY_CREATED = "crm.company.created"
    CRM_COMPANY_UPDATED = "crm.company.updated"
    CRM_COMPANY_DELETED = "crm.company.deleted"
    CRM_CONTACT_CREATED = "crm.contact.created"
    CRM_CONTACT_UPDATED = "crm.contact.updated"
    CRM_CONTACT_DELETED = "crm.contact.deleted"
    CRM_LEAD_CREATED = "crm.lead.created"
    CRM_LEAD_UPDATED = "crm.lead.updated"
    CRM_LEAD_DELETED = "crm.lead.deleted"
    CRM_NOTE_CREATED = "crm.note.created"
    CRM_NOTE_UPDATED = "crm.note.updated"
    CRM_NOTE_DELETED = "crm.note.deleted"
    CRM_OPPORTUNITY_CREATED = "crm.opportunity.created"
    CRM_OPPORTUNITY_UPDATED = "crm.opportunity.updated"
    CRM_OPPORTUNITY_DELETED = "crm.opportunity.deleted"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        crm_activity_created: typing.Callable[[], T_Result],
        crm_activity_updated: typing.Callable[[], T_Result],
        crm_activity_deleted: typing.Callable[[], T_Result],
        crm_company_created: typing.Callable[[], T_Result],
        crm_company_updated: typing.Callable[[], T_Result],
        crm_company_deleted: typing.Callable[[], T_Result],
        crm_contact_created: typing.Callable[[], T_Result],
        crm_contact_updated: typing.Callable[[], T_Result],
        crm_contact_deleted: typing.Callable[[], T_Result],
        crm_lead_created: typing.Callable[[], T_Result],
        crm_lead_updated: typing.Callable[[], T_Result],
        crm_lead_deleted: typing.Callable[[], T_Result],
        crm_note_created: typing.Callable[[], T_Result],
        crm_note_updated: typing.Callable[[], T_Result],
        crm_note_deleted: typing.Callable[[], T_Result],
        crm_opportunity_created: typing.Callable[[], T_Result],
        crm_opportunity_updated: typing.Callable[[], T_Result],
        crm_opportunity_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CrmEventType.ALL:
            return all_()
        if self is CrmEventType.CRM_ACTIVITY_CREATED:
            return crm_activity_created()
        if self is CrmEventType.CRM_ACTIVITY_UPDATED:
            return crm_activity_updated()
        if self is CrmEventType.CRM_ACTIVITY_DELETED:
            return crm_activity_deleted()
        if self is CrmEventType.CRM_COMPANY_CREATED:
            return crm_company_created()
        if self is CrmEventType.CRM_COMPANY_UPDATED:
            return crm_company_updated()
        if self is CrmEventType.CRM_COMPANY_DELETED:
            return crm_company_deleted()
        if self is CrmEventType.CRM_CONTACT_CREATED:
            return crm_contact_created()
        if self is CrmEventType.CRM_CONTACT_UPDATED:
            return crm_contact_updated()
        if self is CrmEventType.CRM_CONTACT_DELETED:
            return crm_contact_deleted()
        if self is CrmEventType.CRM_LEAD_CREATED:
            return crm_lead_created()
        if self is CrmEventType.CRM_LEAD_UPDATED:
            return crm_lead_updated()
        if self is CrmEventType.CRM_LEAD_DELETED:
            return crm_lead_deleted()
        if self is CrmEventType.CRM_NOTE_CREATED:
            return crm_note_created()
        if self is CrmEventType.CRM_NOTE_UPDATED:
            return crm_note_updated()
        if self is CrmEventType.CRM_NOTE_DELETED:
            return crm_note_deleted()
        if self is CrmEventType.CRM_OPPORTUNITY_CREATED:
            return crm_opportunity_created()
        if self is CrmEventType.CRM_OPPORTUNITY_UPDATED:
            return crm_opportunity_updated()
        if self is CrmEventType.CRM_OPPORTUNITY_DELETED:
            return crm_opportunity_deleted()
