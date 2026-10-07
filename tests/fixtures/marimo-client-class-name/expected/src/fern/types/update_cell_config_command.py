

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_cell_config_command_type import UpdateCellConfigCommandType


class UpdateCellConfigCommand(UniversalBaseModel):
    """
    Update cell configuration.

        Updates cell-level settings like disabled state, hide code, etc.

        Attributes:
            configs: Cell IDs mapped to their config updates. Each config dict
                     can contain partial updates.
    """

    configs: typing.Dict[str, typing.Dict[str, typing.Any]]
    type: UpdateCellConfigCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
