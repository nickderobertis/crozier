

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .queue_job_stages_item import QueueJobStagesItem


class QueueJob(UniversalBaseModel):
    current_stage: str
    eta_ms: int
    kit_id: str
    locale: typing.Optional[str] = None
    name: typing.Optional[str] = None
    sku: typing.Optional[str] = None
    stages: typing.List[QueueJobStagesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
