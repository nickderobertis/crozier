

import typing

CrmEventType = typing.Union[
    typing.Literal[
        "*",
        "crm.activity.created",
        "crm.activity.updated",
        "crm.activity.deleted",
        "crm.company.created",
        "crm.company.updated",
        "crm.company.deleted",
        "crm.contact.created",
        "crm.contact.updated",
        "crm.contact.deleted",
        "crm.lead.created",
        "crm.lead.updated",
        "crm.lead.deleted",
        "crm.note.created",
        "crm.note.updated",
        "crm.note.deleted",
        "crm.opportunity.created",
        "crm.opportunity.updated",
        "crm.opportunity.deleted",
    ],
    typing.Any,
]
