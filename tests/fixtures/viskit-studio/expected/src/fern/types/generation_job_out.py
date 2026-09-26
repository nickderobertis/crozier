

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generation_job_out_status import GenerationJobOutStatus
from .generation_output_out import GenerationOutputOut


class GenerationJobOut(UniversalBaseModel):
    cancel_requested: bool
    client_job_id: typing.Optional[str] = None
    created_at: typing.Optional[str] = None
    error_message: typing.Optional[str] = None
    finished_at: typing.Optional[str] = None
    id: str
    locale: str
    marketing_kit_id: typing.Optional[int] = None
    outputs: typing.List[GenerationOutputOut]
    planner_payload: typing.Dict[str, typing.Any]
    source_image_ref: str
    started_at: typing.Optional[str] = None
    status: GenerationJobOutStatus
    updated_at: typing.Optional[str] = None
    user_prompt: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
