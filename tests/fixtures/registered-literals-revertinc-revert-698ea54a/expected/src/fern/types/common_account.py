

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .common_environment import CommonEnvironment


class CommonAccount(UniversalBaseModel):
    id: str
    tenant_count: int
    private_token: str
    public_token: str
    domain: str
    skip_waitlist: typing_extensions.Annotated[
        bool, FieldMetadata(alias="skipWaitlist"), pydantic.Field(alias="skipWaitlist")
    ]
    users: typing.Optional[typing.List["CommonRevertUser"]] = None
    apps: typing.Optional[typing.List["CommonApp"]] = None
    is_onboarding_completed: typing_extensions.Annotated[
        typing.Optional[CommonEnvironment],
        FieldMetadata(alias="isOnboardingCompleted"),
        pydantic.Field(alias="isOnboardingCompleted"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .common_app import CommonApp
from .common_connection import CommonConnection
from .common_revert_user import CommonRevertUser

update_forward_refs(
    CommonAccount, CommonApp=CommonApp, CommonConnection=CommonConnection, CommonRevertUser=CommonRevertUser
)
