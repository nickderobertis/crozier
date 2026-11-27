

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .async_task_errors import AsyncTaskErrors
from .async_task_status import AsyncTaskStatus


class AsyncTask(UniversalBaseModel):
    errors: typing.Optional[AsyncTaskErrors] = None
    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present only when status is FAILED. Contains information about the error.
    """

    response: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Present only when status is SUCCEEDED. response can be empty if there is no data to be returned.
    """

    status: AsyncTaskStatus = pydantic.Field()
    """
    The current state of the task.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
