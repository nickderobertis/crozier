

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pending_invitation_created_by import PendingInvitationCreatedBy


class PendingInvitation(UniversalBaseModel):
    id: str
    role_id: str
    role_name: str
    expires_at: dt.datetime
    created_at: dt.datetime
    created_by: PendingInvitationCreatedBy

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
