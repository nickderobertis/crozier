

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeleteCustomerGroupRequest(UniversalBaseModel):
    """
    Defines the fields that can be included in a request to the
    [DeleteCustomerGroup](https://developer.squareup.com/reference/square_2021-08-18/customer-groups-api/delete-customer-group) endpoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
