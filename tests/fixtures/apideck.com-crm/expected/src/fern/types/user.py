

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .email import Email
from .first_name import FirstName
from .last_name import LastName
from .phone_number import PhoneNumber


class User(UniversalBaseModel):
    addresses: typing.Optional[typing.List[Address]] = None
    company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the company.
    """

    created_at: typing.Optional[str] = None
    department: typing.Optional[str] = pydantic.Field(default=None)
    """
    The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the object.
    """

    division: typing.Optional[str] = pydantic.Field(default=None)
    """
    The division the person is currently in. Usually a collection of departments or teams or regions.
    """

    emails: typing.List[Email]
    employee_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company.
    """

    first_name: typing.Optional[FirstName] = None
    id: typing.Optional[str] = None
    image: typing.Optional[str] = None
    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    language code according to ISO 639-1. For the United States - EN
    """

    last_name: typing.Optional[LastName] = None
    parent_id: typing.Optional[str] = None
    password: typing.Optional[str] = None
    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = None
    status: typing.Optional[str] = None
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The job title of the person.
    """

    updated_at: typing.Optional[str] = None
    username: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
