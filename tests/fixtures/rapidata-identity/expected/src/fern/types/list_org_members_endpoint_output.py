

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_org_members_endpoint_output_member import ListOrgMembersEndpointOutputMember


class ListOrgMembersEndpointOutput(UniversalBaseModel):
    members: typing.List[ListOrgMembersEndpointOutputMember]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
