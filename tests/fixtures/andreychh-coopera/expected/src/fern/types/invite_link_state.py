

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InviteLinkState_Active(UniversalBaseModel):
    status: typing.Literal["active"] = "active"
    expires_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InviteLinkState_Expired(UniversalBaseModel):
    status: typing.Literal["expired"] = "expired"
    expired_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InviteLinkState_Revoked(UniversalBaseModel):
    status: typing.Literal["revoked"] = "revoked"
    revoked_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


InviteLinkState = typing_extensions.Annotated[
    typing.Union[InviteLinkState_Active, InviteLinkState_Expired, InviteLinkState_Revoked],
    pydantic.Field(discriminator="status"),
]
