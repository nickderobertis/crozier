

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_profile_request_role import CreateProfileRequestRole


class CreateProfileRequest(UniversalBaseModel):
    display_name: str
    email: str
    contact_phone: str
    homepage: typing.Optional[str] = None
    callback_url: typing.Optional[str] = None
    birth_date: typing.Optional[dt.date] = None
    last_login_at: typing.Optional[dt.datetime] = None
    avatar_base64: typing.Optional[str] = None
    tenant_host: typing.Optional[str] = None
    source_ip: typing.Optional[str] = None
    login_count: typing.Optional[int] = None
    tags: typing.List[str]
    role: CreateProfileRequestRole

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
