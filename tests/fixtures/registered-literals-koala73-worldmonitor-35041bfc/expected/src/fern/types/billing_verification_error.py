

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .billing_verification_error_code import BillingVerificationErrorCode


class BillingVerificationError(UniversalBaseModel):
    """
    Returned with HTTP 503 when paid access cannot be confirmed right now: the billing provider is re-verifying a recently expired subscription, or the entitlement backend is unreachable. Retryable — honor Retry-After.
    """

    error: str = pydantic.Field()
    """
    Human-readable billing-verification failure reason.
    """

    code: BillingVerificationErrorCode = pydantic.Field()
    """
    Machine-readable billing-verification state, mirrored in the X-Billing-Verification response header.
    """

    required_tier: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="requiredTier"),
        pydantic.Field(
            alias="requiredTier",
            description="Minimum entitlement tier required for this endpoint, when the denial came from a tier gate.",
        ),
    ] = None
    """
    Minimum entitlement tier required for this endpoint, when the denial came from a tier gate.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
