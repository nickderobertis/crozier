

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .common_ticket_priority import CommonTicketPriority
from .common_ticket_status import CommonTicketStatus


class CommonTaskTicketWrite(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the task.
    """

    assignees: typing.List[str] = pydantic.Field()
    """
    collection of IDs belonging to assignees.
    """

    description: str = pydantic.Field()
    """
    Description of the task.
    """

    status: CommonTicketStatus = pydantic.Field()
    """
    Current status of the task.
    """

    priority: CommonTicketPriority = pydantic.Field()
    """
    Priority of the task.
    """

    creator_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="creatorId"), pydantic.Field(alias="creatorId", description="ID of the task creator.")
    ]
    """
    ID of the task creator.
    """

    due_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="dueDate"), pydantic.Field(alias="dueDate", description="Due date for the given task.")
    ]
    """
    Due date for the given task.
    """

    completed_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="completedDate"),
        pydantic.Field(alias="completedDate", description="Date at which task was completed."),
    ]
    """
    Date at which task was completed.
    """

    parent_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId", description="Id of the parent task.")
    ]
    """
    Id of the parent task.
    """

    list_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="listId"), pydantic.Field(alias="listId", description="Id of the list")
    ]
    """
    Id of the list
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
