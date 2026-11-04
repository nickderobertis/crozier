

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .instance_out import InstanceOut
from .model_out import ModelOut


class DeploymentOut(UniversalBaseModel):
    id: str
    model_id: str
    cluster_id: str
    engine: str
    profile: str
    min_replicas: int
    max_replicas: int
    created_at: dt.datetime
    model: typing.Optional[ModelOut] = None
    instances: typing.Optional[typing.List[InstanceOut]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
