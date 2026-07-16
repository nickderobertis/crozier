

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .customer_creation_source_filter import CustomerCreationSourceFilter
from .customer_text_filter import CustomerTextFilter
from .filter_value import FilterValue
from .time_range import TimeRange


class CustomerFilter(UniversalBaseModel):
    """
    Represents a set of `CustomerQuery` filters used to limit the set of
    customers returned by the [SearchCustomers](https://developer.squareup.com/reference/square_2021-08-18/customers-api/search-customers) endpoint.
    """

    created_at: typing.Optional[TimeRange] = None
    creation_source: typing.Optional[CustomerCreationSourceFilter] = None
    email_address: typing.Optional[CustomerTextFilter] = None
    group_ids: typing.Optional[FilterValue] = None
    phone_number: typing.Optional[CustomerTextFilter] = None
    reference_id: typing.Optional[CustomerTextFilter] = None
    updated_at: typing.Optional[TimeRange] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
