

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_organization_members_output_added_users_item import PatchOrganizationMembersOutputAddedUsersItem
from .patch_organization_members_output_status import PatchOrganizationMembersOutputStatus


class PatchOrganizationMembersOutput(UniversalBaseModel):
    status: PatchOrganizationMembersOutputStatus
    org_id: str = pydantic.Field()
    """
    The id of the org that was modified.
    """

    send_email_error: typing.Optional[str] = pydantic.Field(default=None)
    """
    If invite emails failed to send for some reason, the patch operation will still complete, but we will return an error message here
    """

    added_users: typing.Optional[typing.List[PatchOrganizationMembersOutputAddedUsersItem]] = pydantic.Field(
        default=None
    )
    """
    If service accounts with tokens were created, this will contain the added users with their API keys
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
