

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .column_ref import ColumnRef


class ColumnNeighbors(UniversalBaseModel):
    """
    Columns related to ``(dataset, field)`` — its column-level provenance (upstream) or impact.
    """

    dataset: str
    field: str
    related: typing.Optional[typing.List[ColumnRef]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
