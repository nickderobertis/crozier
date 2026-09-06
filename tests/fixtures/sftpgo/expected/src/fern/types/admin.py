

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .admin_filters import AdminFilters
from .admin_group_mapping import AdminGroupMapping
from .admin_permissions import AdminPermissions


class Admin(UniversalBaseModel):
    id: typing.Optional[int] = None
    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    status:
      * `0` user is disabled, login is not allowed
      * `1` user is enabled
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    username is unique
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional description, for example the admin full name
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    Admin password. For security reasons this field is omitted when you search/get admins
    """

    email: typing.Optional[str] = None
    permissions: typing.Optional[typing.List[AdminPermissions]] = None
    filters: typing.Optional[AdminFilters] = None
    additional_info: typing.Optional[str] = pydantic.Field(default=None)
    """
    Free form text field
    """

    groups: typing.Optional[typing.List[AdminGroupMapping]] = pydantic.Field(default=None)
    """
    Groups automatically selected for new users created by this admin. The admin will still be able to choose different groups. These settings are only used for this admin UI and they will be ignored in REST API/hooks.
    """

    created_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    creation time as unix timestamp in milliseconds. It will be 0 for admins created before v2.2.0
    """

    updated_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    last update time as unix timestamp in milliseconds
    """

    last_login: typing.Optional[int] = pydantic.Field(default=None)
    """
    Last user login as unix timestamp in milliseconds. It is saved at most once every 10 minutes
    """

    role: typing.Optional[str] = pydantic.Field(default=None)
    """
    If set the admin can only administer users with the same role. Role admins cannot have the "*" permission
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
