

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .verifier_policy_default_mode import VerifierPolicyDefaultMode


class VerifierPolicy(UniversalBaseModel):
    default_mode: typing.Optional[VerifierPolicyDefaultMode] = None
    risk_overrides: typing.Optional[typing.Dict[str, typing.Any]] = None
    min_classical: typing.Optional[int] = None
    min_pq: typing.Optional[int] = None
    accepted_classical_algs: typing.Optional[typing.List[str]] = None
    accepted_pq_algs: typing.Optional[typing.List[str]] = None
    accepted_hash_algs: typing.Optional[typing.List[str]] = None
    require_session_binding: typing.Optional[bool] = None
    require_composite_binding: typing.Optional[bool] = None
    max_key_age_days: typing.Optional[int] = None
    allow_v1bundles: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allow_v1_bundles"), pydantic.Field(alias="allow_v1_bundles")
    ] = None
    require_session_expiry: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether bundles must include session_expires_at.
    """

    max_session_duration_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum session duration in seconds (0 = no limit).
    """

    require_audience_binding: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether bundles must include intended_verifier matching this verifier.
    """

    verifier_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    This verifier's identity for audience binding checks.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
