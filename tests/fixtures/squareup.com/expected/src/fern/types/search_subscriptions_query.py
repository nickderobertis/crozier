

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .search_subscriptions_filter import SearchSubscriptionsFilter


class SearchSubscriptionsQuery(UniversalBaseModel):
    """
    Represents a query (including filtering criteria) used to search for subscriptions.
    """

    filter: typing.Optional[SearchSubscriptionsFilter] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
