

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .abstract_exchange_type import AbstractExchangeType
from .event_message import EventMessage
from .request import Request
from .response import Response


class Exchange_ReqRespPair(UniversalBaseModel):
    """
    Abstract representation of a Service or API exchange type (request/response, event based, ...)
    """

    type: typing.Literal["reqRespPair"] = "reqRespPair"
    request: Request
    response: Response
    type: AbstractExchangeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Exchange_UnidirEvent(UniversalBaseModel):
    """
    Abstract representation of a Service or API exchange type (request/response, event based, ...)
    """

    type: typing.Literal["unidirEvent"] = "unidirEvent"
    event_message: typing_extensions.Annotated[EventMessage, FieldMetadata(alias="eventMessage")]
    type: AbstractExchangeType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Exchange = typing_extensions.Annotated[
    typing.Union[Exchange_ReqRespPair, Exchange_UnidirEvent], pydantic.Field(discriminator="type")
]
