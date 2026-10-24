

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InviteOrgMemberEndpointOutput(UniversalBaseModel):
    invitation_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="invitationId"),
        pydantic.Field(alias="invitationId", description="The id of the created invitation."),
    ]
    """
    The id of the created invitation.
    """

    token: str = pydantic.Field()
    """
    The single-use token used to accept the invitation.
    """

    expires_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(
            alias="expiresAt", description="The instant after which the invitation can no longer be accepted."
        ),
    ]
    """
    The instant after which the invitation can no longer be accepted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
