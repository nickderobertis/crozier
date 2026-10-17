

import typing

from .twilio_account_connection import TwilioAccountConnection

NormalizedCallTelephonyAccountConnection = typing.Union[str, TwilioAccountConnection]
