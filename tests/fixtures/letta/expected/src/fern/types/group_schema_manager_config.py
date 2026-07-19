

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GroupSchemaManagerConfig_Dynamic(UniversalBaseModel):
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


class GroupSchemaManagerConfig_RoundRobin(UniversalBaseModel):
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


class GroupSchemaManagerConfig_Sleeptime(UniversalBaseModel):
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


class GroupSchemaManagerConfig_Supervisor(UniversalBaseModel):
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


class GroupSchemaManagerConfig_VoiceSleeptime(UniversalBaseModel):
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


GroupSchemaManagerConfig = typing_extensions.Annotated[
    typing.Union[
        GroupSchemaManagerConfig_Dynamic,
        GroupSchemaManagerConfig_RoundRobin,
        GroupSchemaManagerConfig_Sleeptime,
        GroupSchemaManagerConfig_Supervisor,
        GroupSchemaManagerConfig_VoiceSleeptime,
    ],
    pydantic.Field(discriminator="manager_type"),
]
