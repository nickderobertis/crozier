

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .json_duration import JsonDuration


class ClaimResponse(UniversalBaseModel):
    audience: typing.Optional[typing.List[str]] = None
    audience_updated_at: typing.Optional[dt.datetime] = None
    org_id: str
    project_id: typing.Optional[str] = None
    ttl: typing.Optional[JsonDuration] = None
    ttl_updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
