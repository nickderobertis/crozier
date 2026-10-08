

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cell_config import CellConfig
from .cell_id import CellId


class NotebookCell(UniversalBaseModel):
    """
    A single cell in the document. Mutable — owned by the document.

        `version` increments on each `SetCode` that actually changes
        `code`. Other property changes don't bump it.
    """

    code: str
    config: CellConfig
    id: CellId
    name: str
    version: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
