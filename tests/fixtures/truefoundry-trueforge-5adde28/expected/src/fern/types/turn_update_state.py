

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_required import ActionRequired


class TurnUpdateState_Paused(UniversalBaseModel):
    """
    Live non-terminal turn status.
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


class TurnUpdateState_Running(UniversalBaseModel):
    """
    Live non-terminal turn status.
    """

    status: typing.Literal["running"] = "running"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TurnUpdateState = typing_extensions.Annotated[
    typing.Union[TurnUpdateState_Paused, TurnUpdateState_Running], pydantic.Field(discriminator="status")
]
