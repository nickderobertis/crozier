

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .ticket import Ticket
from .ticket_confirmation import TicketConfirmation
from .ticket_message import TicketMessage


class MuseumTicketsConfirmation(Ticket):
    """
    Details for a museum ticket after a successful purchase.
    """

    message: TicketMessage
    confirmation_code: typing_extensions.Annotated[TicketConfirmation, FieldMetadata(alias="confirmationCode")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
