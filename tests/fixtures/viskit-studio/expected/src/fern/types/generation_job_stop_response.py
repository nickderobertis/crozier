

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generation_job_stop_response_status import GenerationJobStopResponseStatus


class GenerationJobStopResponse(UniversalBaseModel):
    cancel_requested: bool
    job_id: str
    status: GenerationJobStopResponseStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
