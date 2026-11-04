

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .forbidden_error_body_code import ForbiddenErrorBodyCode


class ForbiddenErrorBody(UniversalBaseModel):
    """
    Returned when a PRO-gated endpoint denies access because the caller has no resolved authenticated user, entitlements cannot be verified, or the caller lacks the required entitlement tier.
    """

    error: str = pydantic.Field()
    """
    Human-readable entitlement failure reason.
    """

    code: typing.Optional[ForbiddenErrorBodyCode] = pydantic.Field(default=None)
    """
    Machine-readable denial code, present when the 403 is a billing-provider-confirmed subscription lapse (mirrored in the X-Billing-Verification response header).
    """

    required_tier: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="requiredTier"),
        pydantic.Field(alias="requiredTier", description="Minimum entitlement tier required for this endpoint."),
    ] = None
    """
    Minimum entitlement tier required for this endpoint.
    """

    current_tier: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentTier"),
        pydantic.Field(alias="currentTier", description="Caller entitlement tier when known."),
    ] = None
    """
    Caller entitlement tier when known.
    """

    plan_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="planKey"),
        pydantic.Field(alias="planKey", description="Caller plan key when known."),
    ] = None
    """
    Caller plan key when known.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
