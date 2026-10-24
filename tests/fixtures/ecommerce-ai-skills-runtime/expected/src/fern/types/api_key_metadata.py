

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .role import Role


class ApiKeyMetadata(UniversalBaseModel):
    id: str
    key_prefix: str
    created_at: dt.datetime
    revoked_at: typing.Optional[dt.datetime] = None
    user_id: str
    email: str
    role: Role

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
