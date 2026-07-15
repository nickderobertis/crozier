

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .leads_sort_by import LeadsSortBy
from .sort_direction import SortDirection


class LeadsSort(UniversalBaseModel):
    by: typing.Optional[LeadsSortBy] = pydantic.Field(default=None)
    """
    The field on which to sort the Leads
    """

    direction: typing.Optional[SortDirection] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
