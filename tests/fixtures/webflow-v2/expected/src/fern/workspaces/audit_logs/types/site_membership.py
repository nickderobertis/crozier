

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .site_membership_granular_access import SiteMembershipGranularAccess
from .site_membership_method import SiteMembershipMethod
from .site_membership_site import SiteMembershipSite
from .site_membership_target_user import SiteMembershipTargetUser
from .site_membership_user_type import SiteMembershipUserType


class SiteMembership(UniversalBaseModel):
    site: typing.Optional[SiteMembershipSite] = None
    target_user: typing_extensions.Annotated[
        typing.Optional[SiteMembershipTargetUser], FieldMetadata(alias="targetUser"), pydantic.Field(alias="targetUser")
    ] = None
    method: typing.Optional[SiteMembershipMethod] = None
    user_type: typing_extensions.Annotated[
        typing.Optional[SiteMembershipUserType], FieldMetadata(alias="userType"), pydantic.Field(alias="userType")
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

    granular_access: typing_extensions.Annotated[
        typing.Optional[SiteMembershipGranularAccess],
        FieldMetadata(alias="granularAccess"),
        pydantic.Field(alias="granularAccess"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
