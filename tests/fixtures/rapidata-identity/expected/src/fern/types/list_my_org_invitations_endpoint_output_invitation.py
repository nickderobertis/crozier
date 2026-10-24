

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .org_role import OrgRole


class ListMyOrgInvitationsEndpointOutputInvitation(UniversalBaseModel):
    invitation_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="invitationId"), pydantic.Field(alias="invitationId")
    ]
    organization_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="organizationId"), pydantic.Field(alias="organizationId")
    ]
    organization_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="organizationName"), pydantic.Field(alias="organizationName")
    ]
    role: OrgRole
    invited_by_email: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="invitedByEmail"), pydantic.Field(alias="invitedByEmail")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    expires_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
