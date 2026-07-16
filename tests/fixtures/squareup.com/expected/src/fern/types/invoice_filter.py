

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InvoiceFilter(UniversalBaseModel):
    """
    Describes query filters to apply.
    """

    customer_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Limits the search to the specified customers, within the specified locations. 
    Specifying a customer is optional. In the current implementation, 
    a maximum of one customer can be specified.
    """

    location_ids: typing.List[str] = pydantic.Field()
    """
    Limits the search to the specified locations. A location is required. 
    In the current implementation, only one location can be specified.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
