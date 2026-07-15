

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .contact import Contact
from .file import File


class Partner(UniversalBaseModel):
    company: str
    contacts: typing.Optional[typing.List[Contact]] = None
    created_at: typing.Optional[dt.datetime] = None
    icon: typing.Optional[File] = None
    id: typing.Optional[str] = None
    listed: typing.Optional[str] = None
    twitter: typing.Optional[str] = None
    updated_at: typing.Optional[dt.datetime] = None
    website: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
