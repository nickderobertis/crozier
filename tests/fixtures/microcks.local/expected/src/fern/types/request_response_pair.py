

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .abstract_exchange import AbstractExchange
from .request import Request
from .response import Response


class RequestResponsePair(AbstractExchange):
    """
    Request associated with corresponding Response
    """

    request: Request = pydantic.Field()
    """
    The request part of the pair
    """

    response: Response = pydantic.Field()
    """
    The Response part of the pair
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
