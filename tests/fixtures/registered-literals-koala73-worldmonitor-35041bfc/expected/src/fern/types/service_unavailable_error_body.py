

import typing

from .billing_verification_error import BillingVerificationError
from .gateway_error import GatewayError

ServiceUnavailableErrorBody = typing.Union[BillingVerificationError, GatewayError]
