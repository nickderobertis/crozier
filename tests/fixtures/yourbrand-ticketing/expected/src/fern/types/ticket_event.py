

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .project import Project
from .ticket_impact import TicketImpact
from .ticket_participant import TicketParticipant
from .ticket_priority import TicketPriority
from .ticket_status import TicketStatus
from .ticket_urgency import TicketUrgency


class Base(UniversalBaseModel):
    occurred_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="occurredAt"), pydantic.Field(alias="occurredAt")
    ] = None
    tenant_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tenantId"), pydantic.Field(alias="tenantId")
    ] = None
    organization_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="organizationId"), pydantic.Field(alias="organizationId")
    ] = None
    participant: typing.Optional[TicketParticipant] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TicketEvent_TicketCreated(Base):
    event: typing.Literal["TicketCreated"] = "TicketCreated"
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TicketEvent_TicketProjectUpdated(Base):
    event: typing.Literal["TicketProjectUpdated"] = "TicketProjectUpdated"
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    project: typing.Optional[Project] = None
    old_project: typing_extensions.Annotated[
        typing.Optional[Project], FieldMetadata(alias="oldProject"), pydantic.Field(alias="oldProject")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TicketEvent_TicketAssigneeUpdated(Base):
    event: typing.Literal["TicketAssigneeUpdated"] = "TicketAssigneeUpdated"
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    assigned_participant: typing_extensions.Annotated[
        typing.Optional[TicketParticipant],
        FieldMetadata(alias="assignedParticipant"),
        pydantic.Field(alias="assignedParticipant"),
    ] = None
    old_assigned_participant: typing_extensions.Annotated[
        typing.Optional[TicketParticipant],
        FieldMetadata(alias="oldAssignedParticipant"),
        pydantic.Field(alias="oldAssignedParticipant"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TicketEvent_TicketDescriptionUpdated(Base):
    event: typing.Literal["TicketDescriptionUpdated"] = "TicketDescriptionUpdated"
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="newDescription"), pydantic.Field(alias="newDescription")
    ] = None
    old_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="oldDescription"), pydantic.Field(alias="oldDescription")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TicketEvent_TicketEstimatedTimeUpdated(Base):
    event: typing.Literal["TicketEstimatedTimeUpdated"] = "TicketEstimatedTimeUpdated"
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="newTime"), pydantic.Field(alias="newTime")
    ] = None
    old_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="oldTime"), pydantic.Field(alias="oldTime")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TicketEvent_TicketRemainingTimeUpdated(Base):
    event: typing.Literal["TicketRemainingTimeUpdated"] = "TicketRemainingTimeUpdated"
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="newTime"), pydantic.Field(alias="newTime")
    ] = None
    old_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="oldTime"), pydantic.Field(alias="oldTime")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TicketEvent_TicketStatusUpdated(Base):
    event: typing.Literal["TicketStatusUpdated"] = "TicketStatusUpdated"
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_status: typing_extensions.Annotated[
        typing.Optional[TicketStatus], FieldMetadata(alias="newStatus"), pydantic.Field(alias="newStatus")
    ] = None
    old_status: typing_extensions.Annotated[
        typing.Optional[TicketStatus], FieldMetadata(alias="oldStatus"), pydantic.Field(alias="oldStatus")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TicketEvent_TicketSubjectUpdated(Base):
    event: typing.Literal["TicketSubjectUpdated"] = "TicketSubjectUpdated"
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_subject: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="newSubject"), pydantic.Field(alias="newSubject")
    ] = None
    old_subject: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="oldSubject"), pydantic.Field(alias="oldSubject")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TicketEvent_TicketPriorityUpdated(Base):
    event: typing.Literal["TicketPriorityUpdated"] = "TicketPriorityUpdated"
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_priority: typing_extensions.Annotated[
        typing.Optional[TicketPriority], FieldMetadata(alias="newPriority"), pydantic.Field(alias="newPriority")
    ] = None
    old_priority: typing_extensions.Annotated[
        typing.Optional[TicketPriority], FieldMetadata(alias="oldPriority"), pydantic.Field(alias="oldPriority")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TicketEvent_TicketUrgencyUpdated(Base):
    event: typing.Literal["TicketUrgencyUpdated"] = "TicketUrgencyUpdated"
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_urgency: typing_extensions.Annotated[
        typing.Optional[TicketUrgency], FieldMetadata(alias="newUrgency"), pydantic.Field(alias="newUrgency")
    ] = None
    old_urgency: typing_extensions.Annotated[
        typing.Optional[TicketUrgency], FieldMetadata(alias="oldUrgency"), pydantic.Field(alias="oldUrgency")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TicketEvent_TicketImpactUpdated(Base):
    event: typing.Literal["TicketImpactUpdated"] = "TicketImpactUpdated"
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_impact: typing_extensions.Annotated[
        typing.Optional[TicketImpact], FieldMetadata(alias="newImpact"), pydantic.Field(alias="newImpact")
    ] = None
    old_impact: typing_extensions.Annotated[
        typing.Optional[TicketImpact], FieldMetadata(alias="oldImpact"), pydantic.Field(alias="oldImpact")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TicketEvent_TicketCommentAdded(Base):
    event: typing.Literal["TicketCommentAdded"] = "TicketCommentAdded"
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    comment_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="commentId"), pydantic.Field(alias="commentId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TicketEvent = typing_extensions.Annotated[
    typing.Union[
        TicketEvent_TicketCreated,
        TicketEvent_TicketProjectUpdated,
        TicketEvent_TicketAssigneeUpdated,
        TicketEvent_TicketDescriptionUpdated,
        TicketEvent_TicketEstimatedTimeUpdated,
        TicketEvent_TicketRemainingTimeUpdated,
        TicketEvent_TicketStatusUpdated,
        TicketEvent_TicketSubjectUpdated,
        TicketEvent_TicketPriorityUpdated,
        TicketEvent_TicketUrgencyUpdated,
        TicketEvent_TicketImpactUpdated,
        TicketEvent_TicketCommentAdded,
    ],
    pydantic.Field(discriminator="event"),
]
