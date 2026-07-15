

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .first_name import FirstName
from .gender import Gender
from .id import Id
from .last_name import LastName
from .middle_name import MiddleName


class EmployeePartner(UniversalBaseModel):
    birthday: typing.Optional[dt.date] = None
    deceased_on: typing.Optional[dt.date] = None
    first_name: typing.Optional[FirstName] = None
    gender: typing.Optional[Gender] = None
    id: typing.Optional[Id] = None
    initials: typing.Optional[str] = None
    last_name: typing.Optional[LastName] = None
    middle_name: typing.Optional[MiddleName] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
