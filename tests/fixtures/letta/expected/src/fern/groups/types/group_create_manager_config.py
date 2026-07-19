

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GroupCreateManagerConfig_Dynamic(UniversalBaseModel):
    """ """

    manager_type: typing.Literal["dynamic"] = "dynamic"
    manager_agent_id: str
    termination_token: typing.Optional[str] = None
    max_turns: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GroupCreateManagerConfig_RoundRobin(UniversalBaseModel):
    """ """

    manager_type: typing.Literal["round_robin"] = "round_robin"
    max_turns: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GroupCreateManagerConfig_Sleeptime(UniversalBaseModel):
    """ """

    manager_type: typing.Literal["sleeptime"] = "sleeptime"
    manager_agent_id: str
    sleeptime_agent_frequency: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GroupCreateManagerConfig_Supervisor(UniversalBaseModel):
    """ """

    manager_type: typing.Literal["supervisor"] = "supervisor"
    manager_agent_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GroupCreateManagerConfig_VoiceSleeptime(UniversalBaseModel):
    """ """

    manager_type: typing.Literal["voice_sleeptime"] = "voice_sleeptime"
    manager_agent_id: str
    max_message_buffer_length: typing.Optional[int] = None
    min_message_buffer_length: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GroupCreateManagerConfig = typing_extensions.Annotated[
    typing.Union[
        GroupCreateManagerConfig_Dynamic,
        GroupCreateManagerConfig_RoundRobin,
        GroupCreateManagerConfig_Sleeptime,
        GroupCreateManagerConfig_Supervisor,
        GroupCreateManagerConfig_VoiceSleeptime,
    ],
    pydantic.Field(discriminator="manager_type"),
]
