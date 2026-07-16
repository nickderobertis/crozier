

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .card import Card
from .error import Error


class CreateCardResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the [CreateCard](#endpoint-cards-createcard) endpoint.

    Note: if there are errors processing the request, the card field will not be
    present.
    """

    card: typing.Optional[Card] = None
    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information on errors encountered during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
