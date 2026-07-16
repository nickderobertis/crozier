

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AddGroupToCustomerRequest(UniversalBaseModel):
    """
    Defines the fields that are included in the request body of
    a request to the [AddGroupToCustomer](https://developer.squareup.com/reference/square_2021-08-18/customers-api/add-group-to-customer) endpoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
