

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generation_job_created_status import GenerationJobCreatedStatus


class GenerationJobCreated(UniversalBaseModel):
    job_id: str
    output_count: int
    status: GenerationJobCreatedStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
