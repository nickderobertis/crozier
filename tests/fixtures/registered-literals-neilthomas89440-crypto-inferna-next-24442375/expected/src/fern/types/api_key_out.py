

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApiKeyOut(UniversalBaseModel):
    id: str
    user_id: str
    name: str
    scopes: typing.Optional[typing.List[str]] = None
    created_at: dt.datetime
    updated_at: dt.datetime
    last_used_at: typing.Optional[dt.datetime] = None
    revoked_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
