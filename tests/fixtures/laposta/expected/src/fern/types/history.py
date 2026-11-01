

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .history_data_item import HistoryDataItem
from .history_filters import HistoryFilters
from .history_order import HistoryOrder
from .history_pagination import HistoryPagination


class History(UniversalBaseModel):
    """
    A page of events, together with the pagination, sorting and filters that were applied.
    """

    pagination: typing.Optional[HistoryPagination] = None
    order: typing.Optional[HistoryOrder] = None
    filters: typing.Optional[HistoryFilters] = None
    data: typing.Optional[typing.List[HistoryDataItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
