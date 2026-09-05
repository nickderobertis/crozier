

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .acl_object_type import AclObjectType
from .permission import Permission


class Acl(UniversalBaseModel):
    """
    An ACL grants a certain permission or role to a certain user or group on an object.

    ACLs are inherited across the object hierarchy. So for example, if a user has read permissions on a project, they will also have read permissions on any experiment, dataset, etc. created within that project.

    To restrict a grant to a particular sub-object, you may specify `restrict_object_type` in the ACL, as part of a direct permission grant or as part of a role.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the acl
    """

    object_type: AclObjectType
    object_id: str = pydantic.Field()
    """
    The id of the object the ACL applies to
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will be provided
    """

    group_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will be provided
    """

    permission: typing.Optional[Permission] = pydantic.Field(default=None)
    """
    Permission the ACL grants. Exactly one of `permission` and `role_id` will be provided
    """

    restrict_object_type: typing.Optional[AclObjectType] = pydantic.Field(default=None)
    """
    When setting a permission directly, optionally restricts the permission grant to just the specified object type. Cannot be set alongside a `role_id`.
    """

    role_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be provided
    """

    object_org_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="_object_org_id"),
        pydantic.Field(alias="_object_org_id", description="The organization the ACL's referred object belongs to"),
    ]
    """
    The organization the ACL's referred object belongs to
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of acl creation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
