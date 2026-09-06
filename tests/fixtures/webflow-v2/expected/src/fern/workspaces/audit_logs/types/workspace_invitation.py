

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .workspace_invitation_method import WorkspaceInvitationMethod
from .workspace_invitation_target_user import WorkspaceInvitationTargetUser
from .workspace_invitation_target_users_item import WorkspaceInvitationTargetUsersItem
from .workspace_invitation_user_type import WorkspaceInvitationUserType


class WorkspaceInvitation(UniversalBaseModel):
    target_user: typing_extensions.Annotated[
        typing.Optional[WorkspaceInvitationTargetUser],
        FieldMetadata(alias="targetUser"),
        pydantic.Field(alias="targetUser"),
    ] = None
    method: typing.Optional[WorkspaceInvitationMethod] = None
    user_type: typing_extensions.Annotated[
        typing.Optional[WorkspaceInvitationUserType], FieldMetadata(alias="userType"), pydantic.Field(alias="userType")
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

    target_users: typing_extensions.Annotated[
        typing.Optional[typing.List[WorkspaceInvitationTargetUsersItem]],
        FieldMetadata(alias="targetUsers"),
        pydantic.Field(alias="targetUsers"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
