

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AgentEvaluation(UniversalBaseModel):
    id: str
    tenant_id: str
    run_id: str
    evaluator_version: str
    passed: bool
    score: float
    details: typing.Dict[str, typing.Any]
    created_by: str
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
