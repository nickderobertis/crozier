

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule_OneTime(UniversalBaseModel):
    type: typing.Literal["one-time"] = "one-time"
    scheduled_at: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule_Recurring(UniversalBaseModel):
    type: typing.Literal["recurring"] = "recurring"
    cron_expression: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule = typing_extensions.Annotated[
    typing.Union[
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule_OneTime,
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule_Recurring,
    ],
    pydantic.Field(discriminator="type"),
]
