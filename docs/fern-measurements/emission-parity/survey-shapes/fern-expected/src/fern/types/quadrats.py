

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .quadrats_cells_item_item_item import QuadratsCellsItemItemItem
from .quadrats_kind import QuadratsKind


class Quadrats(UniversalBaseModel):
    extent: typing.Optional[typing.List[typing.Any]] = None
    kind: QuadratsKind
    cells: typing.List[typing.List[typing.List[QuadratsCellsItemItemItem]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
