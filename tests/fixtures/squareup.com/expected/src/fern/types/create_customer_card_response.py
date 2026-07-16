

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .card import Card
from .error import Error


class CreateCustomerCardResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the `CreateCustomerCard` endpoint.

    Either `errors` or `card` is present in a given response (never both).
    """

    card: typing.Optional[Card] = None
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
