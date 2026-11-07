

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EmergencyRevokeResponse(UniversalBaseModel):
    ok: typing.Optional[bool] = None
    agent_id: typing.Optional[str] = None
    revoked_at: typing.Optional[dt.datetime] = None
    keys_revoked: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
