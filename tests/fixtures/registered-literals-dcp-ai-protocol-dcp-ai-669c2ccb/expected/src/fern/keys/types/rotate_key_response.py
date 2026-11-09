

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RotateKeyResponse(UniversalBaseModel):
    ok: typing.Optional[bool] = None
    old_kid: typing.Optional[str] = None
    new_kid: typing.Optional[str] = None
    agent_id: typing.Optional[str] = None
    rotated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
