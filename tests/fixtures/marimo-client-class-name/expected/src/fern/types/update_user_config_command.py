

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_config import MarimoConfig
from .update_user_config_command_type import UpdateUserConfigCommandType


class UpdateUserConfigCommand(UniversalBaseModel):
    """
    Update user configuration.

        Updates global marimo configuration (runtime settings, display options, editor preferences).

        Attributes:
            config: Complete user configuration.
    """

    config: MarimoConfig
    type: UpdateUserConfigCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
