

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .membership_status import MembershipStatus
from .org_role import OrgRole


class ListOrgMembersEndpointOutputMember(UniversalBaseModel):
    customer_id: typing_extensions.Annotated[str, FieldMetadata(alias="customerId"), pydantic.Field(alias="customerId")]
    email: typing.Optional[str] = None
    role: OrgRole
    status: MembershipStatus
    is_active_organization_for_member: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isActiveOrganizationForMember"),
        pydantic.Field(alias="isActiveOrganizationForMember"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
