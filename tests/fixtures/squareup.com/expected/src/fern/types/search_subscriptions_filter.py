

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchSubscriptionsFilter(UniversalBaseModel):
    """
    Represents a set of SearchSubscriptionsQuery filters used to limit the set of Subscriptions returned by SearchSubscriptions.
    """

    customer_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A filter to select subscriptions based on the customer.
    """

    location_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A filter to select subscriptions based the location.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
