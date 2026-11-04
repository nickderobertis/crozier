

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipeline_get_by_id_response_errors_item import PipelineGetByIdResponseErrorsItem
from .pipeline_get_by_id_response_state import PipelineGetByIdResponseState
from .pipeline_get_by_id_response_trigger import PipelineGetByIdResponseTrigger
from .pipeline_get_by_id_response_trigger_parameters_value import PipelineGetByIdResponseTriggerParametersValue
from .pipeline_get_by_id_response_vcs import PipelineGetByIdResponseVcs


class PipelineGetByIdResponse(UniversalBaseModel):
    """
    A pipeline response.
    """

    id: str = pydantic.Field()
    """
    The unique ID of the pipeline.
    """

    errors: typing.List[PipelineGetByIdResponseErrorsItem] = pydantic.Field()
    """
    A sequence of errors that have occurred within the pipeline.
    """

    project_slug: str = pydantic.Field()
    """
    The project-slug for the pipeline.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the pipeline was last updated.
    """

    number: int = pydantic.Field()
    """
    The number of the pipeline.
    """

    trigger_parameters: typing.Optional[typing.Dict[str, PipelineGetByIdResponseTriggerParametersValue]] = None
    state: PipelineGetByIdResponseState = pydantic.Field()
    """
    The current state of the pipeline.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The date and time the pipeline was created.
    """

    trigger: PipelineGetByIdResponseTrigger = pydantic.Field()
    """
    A summary of the trigger.
    """

    vcs: typing.Optional[PipelineGetByIdResponseVcs] = pydantic.Field(default=None)
    """
    VCS information for the pipeline.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
