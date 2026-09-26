

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generation_job_start_response_status import GenerationJobStartResponseStatus


class GenerationJobStartResponse(UniversalBaseModel):
    job_id: str
    scheduled: bool
    status: GenerationJobStartResponseStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
