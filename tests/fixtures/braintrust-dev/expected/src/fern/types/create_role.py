

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_role_member_permissions_item import CreateRoleMemberPermissionsItem


class CreateRole(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the role
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the role
    """

    member_permissions: typing.Optional[typing.List[CreateRoleMemberPermissionsItem]] = pydantic.Field(default=None)
    """
    (permission, restrict_object_type) tuples which belong to this role
    """

    member_roles: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Ids of the roles this role inherits from
    
    An inheriting role has all the permissions contained in its member roles, as well as all of their inherited permissions
    """

    org_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the role belongs in.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
