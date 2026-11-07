

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .display_control_action_type import DisplayControlActionType


class DisplayControlAction(UniversalBaseModel):
    """
    A bounded Display Control action. A schedule may contain one action instead of a playlist or Layout. The server validates that only the field belonging to the selected type is present.
    """

    type: DisplayControlActionType
    input: typing.Optional[str] = None
    volume: typing.Optional[int] = None
    brightness: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
