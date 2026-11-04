

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_out import ModelOut


class InstanceOut(UniversalBaseModel):
    id: str
    deployment_id: str
    model_id: str
    cluster_id: str
    worker_id: typing.Optional[str] = None
    engine: str
    profile: str
    gpu_indexes: typing.List[int]
    state: str
    desired_state: str
    generation: int
    port: typing.Optional[int] = None
    error_detail: typing.Optional[str] = None
    created_at: dt.datetime
    updated_at: dt.datetime
    model: typing.Optional[ModelOut] = None
    worker_name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
