

import typing

from .session_begins_payload import SessionBeginsPayload
from .termination_payload import TerminationPayload
from .turn_payload import TurnPayload

ReceivePayload = typing.Union[SessionBeginsPayload, TurnPayload, TerminationPayload]
