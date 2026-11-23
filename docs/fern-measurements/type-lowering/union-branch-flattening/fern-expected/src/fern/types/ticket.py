

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ticket_fare import TicketFare


class Ticket(UniversalBaseModel):
    """
    Inline anyOf branches.
    """

    code: typing.Optional[str] = None
    fare: typing.Optional[TicketFare] = None
    price: typing.Optional[str] = None
    seat: typing.Optional[str] = None
    guardian: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
