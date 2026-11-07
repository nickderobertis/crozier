

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_required import ActionRequired


class TurnUpdateEventState_Paused(UniversalBaseModel):
    """
    Live non-terminal turn state (paused or running).
    """

    status: typing.Literal["paused"] = "paused"
    action_required_on_events: typing.List[ActionRequired]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TurnUpdateEventState_Running(UniversalBaseModel):
    """
    Live non-terminal turn state (paused or running).
    """

    status: typing.Literal["running"] = "running"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TurnUpdateEventState = typing_extensions.Annotated[
    typing.Union[TurnUpdateEventState_Paused, TurnUpdateEventState_Running], pydantic.Field(discriminator="status")
]
