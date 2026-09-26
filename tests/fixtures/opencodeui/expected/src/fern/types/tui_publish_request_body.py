

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_tui_command_execute_properties import EventTuiCommandExecuteProperties
from .event_tui_prompt_append_properties import EventTuiPromptAppendProperties
from .event_tui_session_select_properties import EventTuiSessionSelectProperties
from .event_tui_toast_show_properties import EventTuiToastShowProperties


class TuiPublishRequestBody_TuiPromptAppend(UniversalBaseModel):
    type: typing.Literal["tui.prompt.append"] = "tui.prompt.append"
    properties: EventTuiPromptAppendProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TuiPublishRequestBody_TuiCommandExecute(UniversalBaseModel):
    type: typing.Literal["tui.command.execute"] = "tui.command.execute"
    properties: EventTuiCommandExecuteProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TuiPublishRequestBody_TuiToastShow(UniversalBaseModel):
    type: typing.Literal["tui.toast.show"] = "tui.toast.show"
    properties: EventTuiToastShowProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TuiPublishRequestBody_TuiSessionSelect(UniversalBaseModel):
    type: typing.Literal["tui.session.select"] = "tui.session.select"
    properties: EventTuiSessionSelectProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TuiPublishRequestBody = typing_extensions.Annotated[
    typing.Union[
        TuiPublishRequestBody_TuiPromptAppend,
        TuiPublishRequestBody_TuiCommandExecute,
        TuiPublishRequestBody_TuiToastShow,
        TuiPublishRequestBody_TuiSessionSelect,
    ],
    pydantic.Field(discriminator="type"),
]
