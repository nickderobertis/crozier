

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bills_sort_by import BillsSortBy
from .sort_direction import SortDirection


class BillsSort(UniversalBaseModel):
    by: typing.Optional[BillsSortBy] = pydantic.Field(default=None)
    """
    The field on which to sort the Bills
    """

    direction: typing.Optional[SortDirection] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
