

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UserUpdateOwnProfileResponse(UniversalBaseModel):
    organization_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="organizationName"), pydantic.Field(alias="organizationName")
    ]
    invitation_expires_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="invitationExpiresUtc"),
        pydantic.Field(
            alias="invitationExpiresUtc",
            description="Read off the outstanding invitation rather than worked out from `invitedUtc` and the\nconfigured lifetime: the link's expiry was fixed when it was issued, so reconfiguring\nthat lifetime cannot retroactively expire or revive one. At most one invitation is\noutstanding per user, because issuing a new one retires the last.",
        ),
    ] = None
    """
    Read off the outstanding invitation rather than worked out from `invitedUtc` and the
    configured lifetime: the link's expiry was fixed when it was issued, so reconfiguring
    that lifetime cannot retroactively expire or revive one. At most one invitation is
    outstanding per user, because issuing a new one retires the last.
    """

    id: str
    organization_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="organizationId"), pydantic.Field(alias="organizationId")
    ]
    email: str
    name: str
    role: str
    status: str
    created_utc: typing_extensions.Annotated[str, FieldMetadata(alias="createdUtc"), pydantic.Field(alias="createdUtc")]
    invited_utc: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="invitedUtc"), pydantic.Field(alias="invitedUtc")
    ] = None
    activated_utc: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="activatedUtc"), pydantic.Field(alias="activatedUtc")
    ] = None
    last_login_utc: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastLoginUtc"), pydantic.Field(alias="lastLoginUtc")
    ] = None
    deleted_utc: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="deletedUtc"), pydantic.Field(alias="deletedUtc")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
