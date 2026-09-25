

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1users_create_user_capacity import V1UsersCreateUserCapacity
from .v1users_create_user_projects import V1UsersCreateUserProjects
from .v1users_create_user_properties_attributes_item import V1UsersCreateUserPropertiesAttributesItem
from .v1users_create_user_user_level import V1UsersCreateUserUserLevel


class V1UsersCreateUser(UniversalBaseModel):
    admin: typing.Optional[bool] = pydantic.Field(default=None)
    """
    **(Deprecated)**  
                          Requires admin role
    """

    hide_hourly_rate: typing.Optional[bool] = None
    hide_internal_hourly_rate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The hide_internal_hourly_rate hides the internal hourly rate for users in the account. The default is **true**
    """

    default_hour_rate: typing.Optional[int] = None
    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Can be used to reference external resource IDs to Timely resources
    """

    weekly_capacity: typing.Optional[int] = pydantic.Field(default=None)
    """
    Specifies the user's weekly hour capacity. The default is account's weekly capacity. Can only have a decimal place of .5 (e.g. 3.5 hours)
    """

    team_ids: typing.Optional[int] = None
    internal_hour_rate: typing.Optional[int] = pydantic.Field(default=None)
    """
    Specifies the internal hourly rate for user
    """

    add_to_all_projects: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Specifies whether the user should be added to all projects in the account
    """

    apply_default_rate: typing.Optional[bool] = None
    capacity: typing.Optional[V1UsersCreateUserCapacity] = None
    properties_attributes: typing.Optional[typing.List[V1UsersCreateUserPropertiesAttributesItem]] = pydantic.Field(
        default=None
    )
    """
    Array item can describe **update** | **delete** | **create** actions
    """

    projects: typing.Optional[V1UsersCreateUserProjects] = None
    user_level: typing.Optional[V1UsersCreateUserUserLevel] = pydantic.Field(default=None)
    """
    **(Deprecated)**  
                             Specifies the user level  
                             Required if **role_id** is blank.  
                             Must be **normal** if **role_id** is blank and **admin** is true  
                             Must be **limited** if **role_id** is blank and **hide_hourly_rate** is true  
                             Must be **limited** if **role_id** is blank and **hide_internal_hourly_rate** is true"
    """

    role_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Specifies the user's role in the account. Required if **user_level** is blank
    """

    name: str
    email: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
