

import typing

from .approval_interaction import ApprovalInteraction
from .authentication_interaction import AuthenticationInteraction
from .payment_interaction import PaymentInteraction
from .verification_interaction import VerificationInteraction

ActActionResponseInteraction = typing.Union[
    AuthenticationInteraction, PaymentInteraction, ApprovalInteraction, VerificationInteraction
]
