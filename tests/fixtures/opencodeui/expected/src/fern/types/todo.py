

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Todo(UniversalBaseModel):
    content: str = pydantic.Field()
    """
    Brief description of the task
    """

    status: str = pydantic.Field()
    """
    Current status of the task: pending, in_progress, completed, cancelled
    """

    priority: str = pydantic.Field()
    """
    Priority level of the task: high, medium, low
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the todo item
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
