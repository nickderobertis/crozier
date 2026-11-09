

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterGovernanceResponse(UniversalBaseModel):
    ok: typing.Optional[bool] = None
    governance_id: typing.Optional[str] = None
    threshold: typing.Optional[int] = None
    key_count: typing.Optional[int] = None
    registered_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
