

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1EmployeeRole(UniversalBaseModel):
    """
    V1EmployeeRole
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the employee entity was created, in ISO 8601 format. Is set by Square when the Role is created.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The role's unique ID, Can only be set by Square.
    """

    is_owner: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, employees with this role have all permissions, regardless of the values indicated in permissions.
    """

    name: str = pydantic.Field()
    """
    The role's merchant-defined name.
    """

    permissions: typing.List[str] = pydantic.Field()
    """
    The role's permissions.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the employee entity was most recently updated, in ISO 8601 format. Is set by Square when the Role updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
