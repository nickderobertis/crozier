

import typing

LeadEventType = typing.Union[
    typing.Literal["*", "lead.lead.created", "lead.lead.updated", "lead.lead.deleted"], typing.Any
]
