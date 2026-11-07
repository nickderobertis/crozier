

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonTaskRead(UniversalBaseModel):
    subject: str = pydantic.Field()
    """
    Subject of the task.
    """

    body: str = pydantic.Field()
    """
    Body of the task description.
    """

    priority: str = pydantic.Field()
    """
    The priority of the task in hand. (not supported by pipedrive)
    """

    status: str = pydantic.Field()
    """
    Completion status of the task.
    """

    due_date: typing_extensions.Annotated[typing.Any, FieldMetadata(alias="dueDate"), pydantic.Field(alias="dueDate")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
