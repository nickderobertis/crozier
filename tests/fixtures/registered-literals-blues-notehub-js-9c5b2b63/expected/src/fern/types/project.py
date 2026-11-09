

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .contact import Contact
from .role import Role


class Project(UniversalBaseModel):
    administrative_contact: typing.Optional[Contact] = None
    created: dt.datetime
    label: str
    role: typing.Optional[Role] = None
    technical_contact: typing.Optional[Contact] = None
    uid: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
