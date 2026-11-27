

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .org_membership_collaborator_role import OrgMembershipCollaboratorRole
from .org_membership_collaborator_type import OrgMembershipCollaboratorType
from .organization_summary import OrganizationSummary


class OrgMembershipCollaborator(UniversalBaseModel):
    organization: typing.Optional[OrganizationSummary] = None
    role: typing.Optional[OrgMembershipCollaboratorRole] = None
    type: typing.Optional[OrgMembershipCollaboratorType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
