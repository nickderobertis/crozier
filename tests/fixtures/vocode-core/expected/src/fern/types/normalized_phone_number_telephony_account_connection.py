

import typing

from .twilio_account_connection import TwilioAccountConnection

NormalizedPhoneNumberTelephonyAccountConnection = typing.Union[str, TwilioAccountConnection]
