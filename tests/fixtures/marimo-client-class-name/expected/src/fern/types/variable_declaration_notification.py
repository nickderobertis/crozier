

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cell_id import CellId
from .variable_name import VariableName


class VariableDeclarationNotification(UniversalBaseModel):
    """
    Variable declaration and usage for dataflow graph.

        Attributes:
            name: Variable name.
            declared_by: Cell IDs that define this variable.
            used_by: Cell IDs that use this variable.
    """

    declared_by: typing.List[CellId]
    name: VariableName
    used_by: typing.List[CellId]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
