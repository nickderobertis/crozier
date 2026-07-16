

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1Employee(UniversalBaseModel):
    """
    Represents one of a business's employees.
    """

    authorized_location_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The IDs of the locations the employee is allowed to clock in at.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the employee entity was created, in ISO 8601 format.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The employee's email address.
    """

    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An ID the merchant can set to associate the employee with an entity in another system.
    """

    first_name: str = pydantic.Field()
    """
    The employee's first name.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The employee's unique ID.
    """

    last_name: str = pydantic.Field()
    """
    The employee's last name.
    """

    role_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The ids of the employee's associated roles. Currently, you can specify only one or zero roles per employee.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Whether the employee is ACTIVE or INACTIVE. Inactive employees cannot sign in to Square Register.Merchants update this field from the Square Dashboard.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the employee entity was most recently updated, in ISO 8601 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
