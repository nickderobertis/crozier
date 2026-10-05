

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .task_status import TaskStatus


class OpenShiftNamespacesTaskResponse(UniversalBaseModel):
    """
    Response for POST /reconcile (202 Accepted).
    """

    id: str = pydantic.Field()
    """
    Task ID
    """

    status: TaskStatus = pydantic.Field()
    """
    Initial task status
    """

    status_url: str = pydantic.Field()
    """
    URL to poll for task result
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
