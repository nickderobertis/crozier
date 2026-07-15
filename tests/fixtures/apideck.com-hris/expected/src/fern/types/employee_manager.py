

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employment_status import EmploymentStatus
from .first_name import FirstName
from .id import Id
from .last_name import LastName


class EmployeeManager(UniversalBaseModel):
    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address of the manager.
    """

    employment_status: typing.Optional[EmploymentStatus] = None
    first_name: typing.Optional[FirstName] = None
    id: typing.Optional[Id] = None
    last_name: typing.Optional[LastName] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the manager, often a combination of their first and last names.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
