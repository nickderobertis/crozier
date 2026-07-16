

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .shift_filter import ShiftFilter
from .shift_sort import ShiftSort


class ShiftQuery(UniversalBaseModel):
    """
    The parameters of a `Shift` search query, which includes filter and sort options.
    """

    filter: typing.Optional[ShiftFilter] = None
    sort: typing.Optional[ShiftSort] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
