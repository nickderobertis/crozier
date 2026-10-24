

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_org_invitations_endpoint_output_invitation import ListOrgInvitationsEndpointOutputInvitation


class ListOrgInvitationsEndpointOutput(UniversalBaseModel):
    invitations: typing.List[ListOrgInvitationsEndpointOutputInvitation]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
