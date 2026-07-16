

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .customer_filter import CustomerFilter
from .customer_sort import CustomerSort


class CustomerQuery(UniversalBaseModel):
    """
    Represents a query (including filtering criteria, sorting criteria, or both) used to search
    for customer profiles.
    """

    filter: typing.Optional[CustomerFilter] = None
    sort: typing.Optional[CustomerSort] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
