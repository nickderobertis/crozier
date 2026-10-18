

import typing

from .twilio_credentials import TwilioCredentials
from .undefined import Undefined

TwilioAccountConnectionUpdateParamsCredentials = typing.Union[TwilioCredentials, Undefined]
