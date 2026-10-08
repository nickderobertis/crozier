

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cell_id import CellId
from .multiple_definition_error_type import MultipleDefinitionErrorType


class MultipleDefinitionError(UniversalBaseModel):
    cells: typing.List[CellId]
    name: str
    type: MultipleDefinitionErrorType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
