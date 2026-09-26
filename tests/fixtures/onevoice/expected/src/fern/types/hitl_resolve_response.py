

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .hitl_resolved_call import HitlResolvedCall


class HitlResolveResponse(UniversalBaseModel):
    batch_id: str
    resolved_at: dt.datetime
    decisions: typing.List[HitlResolvedCall]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
