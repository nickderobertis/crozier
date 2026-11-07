

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workflow_get_by_id_response_status import WorkflowGetByIdResponseStatus
from .workflow_get_by_id_response_tag import WorkflowGetByIdResponseTag


class WorkflowGetByIdResponse(UniversalBaseModel):
    """
    A workflow
    """

    pipeline_id: str = pydantic.Field()
    """
    The ID of the pipeline this workflow belongs to.
    """

    canceled_by: typing.Optional[str] = None
    id: str = pydantic.Field()
    """
    The unique ID of the workflow.
    """

    name: str = pydantic.Field()
    """
    The name of the workflow.
    """

    project_slug: str = pydantic.Field()
    """
    The project-slug for the pipeline this workflow belongs to.
    """

    errored_by: typing.Optional[str] = None
    tag: typing.Optional[WorkflowGetByIdResponseTag] = pydantic.Field(default=None)
    """
    Tag used for the workflow
    """

    status: WorkflowGetByIdResponseStatus = pydantic.Field()
    """
    The current status of the workflow.
    """

    started_by: str
    pipeline_number: int = pydantic.Field()
    """
    The number of the pipeline this workflow belongs to.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The date and time the workflow was created.
    """

    stopped_at: dt.datetime = pydantic.Field()
    """
    The date and time the workflow stopped.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
