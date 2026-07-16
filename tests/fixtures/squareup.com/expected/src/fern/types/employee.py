

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Employee(UniversalBaseModel):
    """
    An employee object that is used by the external API.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A read-only timestamp in RFC 3339 format.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The employee's email address
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The employee's first name.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    UUID for this object.
    """

    is_owner: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this employee is the owner of the merchant. Each merchant
    has one owner employee, and that employee has full authority over
    the account.
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The employee's last name.
    """

    location_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of location IDs where this employee has access to.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The employee's phone number in E.164 format, i.e. "+12125554250"
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies the status of the employees being fetched.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A read-only timestamp in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
