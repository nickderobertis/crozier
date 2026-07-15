

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assignee import Assignee
from .collection_tag import CollectionTag
from .created_at import CreatedAt
from .created_by import CreatedBy
from .id import Id
from .ticket_priority import TicketPriority
from .updated_at import UpdatedAt


class Ticket(UniversalBaseModel):
    assignees: typing.Optional[typing.List[Assignee]] = None
    collection_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ticket's collection ID
    """

    completed_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the ticket was completed
    """

    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ticket's description. HTML version of description is mapped if supported by the third-party platform
    """

    due_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Due date of the ticket
    """

    id: typing.Optional[Id] = None
    parent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ticket's parent ID
    """

    priority: typing.Optional[TicketPriority] = pydantic.Field(default=None)
    """
    Priority of the ticket
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through.
    """

    subject: typing.Optional[str] = pydantic.Field(default=None)
    """
    Subject of the ticket
    """

    tags: typing.Optional[typing.List[CollectionTag]] = None
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ticket's type
    """

    updated_at: typing.Optional[UpdatedAt] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
