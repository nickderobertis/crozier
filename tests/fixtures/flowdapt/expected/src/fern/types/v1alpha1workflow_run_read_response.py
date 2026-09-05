

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1Alpha1WorkflowRunReadResponse(UniversalBaseModel):
    uid: str
    name: str
    workflow: str
    started_at: dt.datetime
    finished_at: typing.Optional[dt.datetime] = None
    result: typing.Optional[typing.Any] = None
    state: str
    source: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
