

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .role_member_permissions_item import RoleMemberPermissionsItem


class Role(UniversalBaseModel):
    """
    A role is a collection of permissions which can be granted as part of an ACL

    Roles can consist of individual permissions, as well as a set of roles they inherit from
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the role
    """

    org_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique id for the organization that the role belongs under
    
    A null org_id indicates a system role, which may be assigned to anybody and inherited by any other role, but cannot be edited.
    
    It is forbidden to change the org after creating a role
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies the user who created the role
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of role creation
    """

    name: str = pydantic.Field()
    """
    Name of the role
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the role
    """

    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of role deletion, or null if the role is still active
    """

    member_permissions: typing.Optional[typing.List[RoleMemberPermissionsItem]] = pydantic.Field(default=None)
    """
    (permission, restrict_object_type) tuples which belong to this role
    """

    member_roles: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Ids of the roles this role inherits from
    
    An inheriting role has all the permissions contained in its member roles, as well as all of their inherited permissions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
