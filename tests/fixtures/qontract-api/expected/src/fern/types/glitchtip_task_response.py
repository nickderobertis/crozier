

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .task_status import TaskStatus


class GlitchtipTaskResponse(UniversalBaseModel):
    """
    Response model for POST /reconcile endpoint.
    """

    id: str = pydantic.Field()
    """
    Task ID
    """

    status: typing.Optional[TaskStatus] = pydantic.Field(default=None)
    """
    Task status (always 'pending' initially)
    """

    status_url: str = pydantic.Field()
    """
    URL to retrieve task result (GET request)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
