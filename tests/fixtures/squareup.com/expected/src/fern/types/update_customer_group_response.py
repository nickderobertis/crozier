

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .customer_group import CustomerGroup
from .error import Error


class UpdateCustomerGroupResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the [UpdateCustomerGroup](https://developer.squareup.com/reference/square_2021-08-18/customer-groups-api/update-customer-group) endpoint.

    Either `errors` or `group` is present in a given response (never both).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    group: typing.Optional[CustomerGroup] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
