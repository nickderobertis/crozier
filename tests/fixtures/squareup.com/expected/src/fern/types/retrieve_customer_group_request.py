

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RetrieveCustomerGroupRequest(UniversalBaseModel):
    """
    Defines the fields that can be included in a request to the
    [RetrieveCustomerGroup](https://developer.squareup.com/reference/square_2021-08-18/customer-groups-api/retrieve-customer-group) endpoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
