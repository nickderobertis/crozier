

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .workspace_membership_method import WorkspaceMembershipMethod
from .workspace_membership_target_user import WorkspaceMembershipTargetUser
from .workspace_membership_user_type import WorkspaceMembershipUserType


class WorkspaceMembership(UniversalBaseModel):
    target_user: typing_extensions.Annotated[
        typing.Optional[WorkspaceMembershipTargetUser],
        FieldMetadata(alias="targetUser"),
        pydantic.Field(alias="targetUser"),
    ] = None
    method: typing.Optional[WorkspaceMembershipMethod] = None
    user_type: typing_extensions.Annotated[
        typing.Optional[WorkspaceMembershipUserType], FieldMetadata(alias="userType"), pydantic.Field(alias="userType")
    ] = None
    role_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="roleName"),
        pydantic.Field(alias="roleName", description="The name of the role that was assigned to the user"),
    ] = None
    """
    The name of the role that was assigned to the user
    """

    previous_role_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="previousRoleName"),
        pydantic.Field(alias="previousRoleName", description="The previous role that the user had"),
    ] = None
    """
    The previous role that the user had
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
