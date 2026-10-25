

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.sha256 import Sha256


class UseAgentInvitationRequest_Join(UniversalBaseModel):
    action: typing.Literal["join"] = "join"
    invitation: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UseAgentInvitationRequest_Say(UniversalBaseModel):
    action: typing.Literal["say"] = "say"
    invitation: str
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UseAgentInvitationRequest_Check(UniversalBaseModel):
    action: typing.Literal["check"] = "check"
    invitation: str
    after: typing.Optional[int] = None
    wait_seconds: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UseAgentInvitationRequest_Finish(UniversalBaseModel):
    action: typing.Literal["finish"] = "finish"
    invitation: str
    markdown: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UseAgentInvitationRequest_Final(UniversalBaseModel):
    action: typing.Literal["final"] = "final"
    invitation: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UseAgentInvitationRequest_Collect(UniversalBaseModel):
    action: typing.Literal["collect"] = "collect"
    invitation: str
    sha256: Sha256

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UseAgentInvitationRequest_Close(UniversalBaseModel):
    action: typing.Literal["close"] = "close"
    invitation: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UseAgentInvitationRequest = typing_extensions.Annotated[
    typing.Union[
        UseAgentInvitationRequest_Join,
        UseAgentInvitationRequest_Say,
        UseAgentInvitationRequest_Check,
        UseAgentInvitationRequest_Finish,
        UseAgentInvitationRequest_Final,
        UseAgentInvitationRequest_Collect,
        UseAgentInvitationRequest_Close,
    ],
    pydantic.Field(discriminator="action"),
]
