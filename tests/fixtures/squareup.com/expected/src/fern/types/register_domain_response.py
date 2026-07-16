

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error


class RegisterDomainResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the [RegisterDomain](https://developer.squareup.com/reference/square_2021-08-18/apple-pay-api/register-domain) endpoint.

    Either `errors` or `status` are present in a given response (never both).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the domain registration.
    
    See [RegisterDomainResponseStatus](https://developer.squareup.com/reference/square_2021-08-18/enums/RegisterDomainResponseStatus) for possible values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
