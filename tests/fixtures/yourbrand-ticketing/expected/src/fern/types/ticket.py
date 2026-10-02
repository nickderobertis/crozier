

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attachment import Attachment
from .project import Project
from .tag import Tag
from .ticket_impact import TicketImpact
from .ticket_participant import TicketParticipant
from .ticket_priority import TicketPriority
from .ticket_status import TicketStatus
from .ticket_type import TicketType
from .ticket_urgency import TicketUrgency


class Ticket(UniversalBaseModel):
    id: typing.Optional[int] = None
    project: typing.Optional[Project] = None
    subject: typing.Optional[str] = None
    description: typing.Optional[str] = None
    status: typing.Optional[TicketStatus] = None
    assignee: typing.Optional[TicketParticipant] = None
    last_message: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastMessage"), pydantic.Field(alias="lastMessage")
    ] = None
    text: typing.Optional[str] = None
    type: typing.Optional[TicketType] = None
    priority: typing.Optional[TicketPriority] = None
    urgency: typing.Optional[TicketUrgency] = None
    impact: typing.Optional[TicketImpact] = None
    estimated_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="estimatedTime"), pydantic.Field(alias="estimatedTime")
    ] = None
    completed_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="completedTime"), pydantic.Field(alias="completedTime")
    ] = None
    remaining_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="remainingTime"), pydantic.Field(alias="remainingTime")
    ] = None
    planned_start_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="plannedStartDate"), pydantic.Field(alias="plannedStartDate")
    ] = None
    start_deadline: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startDeadline"), pydantic.Field(alias="startDeadline")
    ] = None
    expected_end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expectedEndDate"), pydantic.Field(alias="expectedEndDate")
    ] = None
    due_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="dueDate"), pydantic.Field(alias="dueDate")
    ] = None
    actual_start_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="actualStartDate"), pydantic.Field(alias="actualStartDate")
    ] = None
    actual_end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="actualEndDate"), pydantic.Field(alias="actualEndDate")
    ] = None
    tags: typing.Optional[typing.List[Tag]] = None
    attachments: typing.Optional[typing.List[Attachment]] = None
    created: typing.Optional[dt.datetime] = None
    created_by: typing_extensions.Annotated[
        typing.Optional[TicketParticipant], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    last_modified: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ] = None
    last_modified_by: typing_extensions.Annotated[
        typing.Optional[TicketParticipant],
        FieldMetadata(alias="lastModifiedBy"),
        pydantic.Field(alias="lastModifiedBy"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
