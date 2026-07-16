

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .customer import Customer
from .error import Error


class UpdateCustomerResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the `UpdateCustomer` endpoint.

    Either `errors` or `customer` is present in a given response (never both).
    """

    customer: typing.Optional[Customer] = None
    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
